from django.db import models
from customers.models import Customer
from books.models import Book

class Order(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
        books = models.ManyToManyField(Book, through='OrderItem')
        total_amount = models.DecimalField(max_digits=10, decimal_places=2)
        discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
        created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        book = models.ForeignKey(Book, on_delete=models.CASCADE)
        quantity = models.IntegerField()