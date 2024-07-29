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


class Projects(models.Model):
    """
    Loyihalar uchun model
    """
    subcategories = models.ForeignKey(SubCategories, on_delete=models.SET_NULL, blank=True, null=True,
                                      verbose_name="Pastgi Kategoriyalar")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nomi", db_index=True)
    subject = models.TextField(verbose_name="Izoh")
    files = models.ManyToManyField("Files", verbose_name="Loyiha fayillari")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return f"{self.subcategories} -- {self.name}"

    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"


class Files(models.Model):
    """
    Loyiha Fayllari uchun model
    """
    file_code = models.CharField(max_length=25, verbose_name="Fayil Kodi")
    file = models.FileField(upload_to="file", verbose_name="Fayl")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return f"Fayil kodi: {self.file_code}"

    class Meta:
        verbose_name = "Fayil"
        verbose_name_plural = "Loyiha Fayillari"