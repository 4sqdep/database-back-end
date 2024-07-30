from django.db import models
from django.contrib.auth.models import AbstractUser, Permission



# Foydalanuvchi uchun maxsuss rollar yaratish
class Role(models.Model):
    name = models.CharField(max_length=255, verbose_name="Rol nomi")
    permissions = models.ManyToManyField(Permission, blank=True, verbose_name="Permishnlar")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Rollar"


# Foydalanuvchilar
class User(AbstractUser):
    role = models.ManyToManyField(Role, blank=True, related_name='users', verbose_name="Rollar")
    is_director = models.BooleanField(default=False, verbose_name="Director")
    is_designer = models.BooleanField(default=False, verbose_name="Loyihachi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"