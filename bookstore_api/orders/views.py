from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer
from books.models import Book
import os
from decimal import Decimal
from bookstore_api.authentication import CustomerTokenAuthentication

class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomerTokenAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def place_order(self, request):
        customer = request.user.customer
        books_data = request.data.get('books', [])
        
        if not books_data:
            return Response({"error": "No books provided"}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = 0
        order_items = []

        for book_data in books_data:
            book_id = book_data.get('id')
            quantity = book_data.get('quantity', 1)

            try:
                book = Book.objects.get(id=book_id)
            except Book.DoesNotExist:
                return Response({"error": f"Book with id {book_id} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            if book.stock < quantity:
                return Response({"error": f"Not enough stock for book {book.title}"}, status=status.HTTP_400_BAD_REQUEST)

            total_amount += book.price * quantity
            order_items.append({'book': book, 'quantity': quantity})

        # Apply discount for first-time customers
        discount_amount = 0
        if not Order.objects.filter(customer=customer).exists():
            discount_type = os.getenv('DISCOUNT_TYPE', 'PERCENTAGE')
            discount_value = Decimal(os.getenv('DISCOUNT_VALUE', '10'))
            
            if discount_type == 'PERCENTAGE':
                discount_amount = total_amount * (discount_value / 100)
            else:
                discount_amount = discount_value

        order = Order.objects.create(customer=customer, total_amount=total_amount - discount_amount, discount_amount=discount_amount)

        for item in order_items:
            OrderItem.objects.create(order=order, book=item['book'], quantity=item['quantity'])
            item['book'].stock -= item['quantity']
            item['book'].save()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)