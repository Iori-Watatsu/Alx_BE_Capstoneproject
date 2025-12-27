from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if username is None or password is None:
            return None

        try:
            user = user.objects.get(email__iexact=username)
        except user.DoesNotExits:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def get_user(selfself, user_id):
        try:
            return user.objects.get(pk=user_id)
        except user.DoesNotExits:
            return None

    def user_can_authenticate(selfself, user):
        return getattr(user, "is_active", True)