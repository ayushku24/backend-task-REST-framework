from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class AuthorTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if not hasattr(user, 'author'):
            raise AuthenticationFailed('User is not an author')
        return user, token

class CustomerTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if not hasattr(user, 'customer'):
            raise AuthenticationFailed('User is not a customer')
        return user, token