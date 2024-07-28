from django.db import models
from account.models import User



class Categories(models.Model):
    """
    Kategoriyalar uchun model
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Foydalanuvchi")
    name = models.CharField(max_length=500, verbose_name="Nomi", blank=True, null=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return f"{self.user} -- {self.name}"

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class SubCategories(models.Model):
    """
    Pastgi Kategorialar uchun model
    """
    categories = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Kategoriyalar")
    name = models.CharField(max_length=500, blank=True, null=True, verbose_name="Nomi", db_index=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name="Pastgi Kategoriyalar bolalari")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return f"{self.categories} -- {self.name}"

    class Meta:
        verbose_name = "Pastgi Kategoriya"
        verbose_name_plural = "Pastgi Kategoriyalar"