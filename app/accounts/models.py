from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "auth_user"
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"
