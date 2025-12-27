from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if username is None or password is None:
            return None

        try:
            user = User.objects.get(email__iexact=username)
        except User.DoesNotExist:
            return None

        if User.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def get_user(selfself, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExits:
            return None

    def user_can_authenticate(selfself, user):
        return getattr(user, "is_active", True)