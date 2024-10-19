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
        return f"{self.name}"

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class SubCategories(models.Model):
    """
    Pastgi Kategorialar uchun model
    """
    categories = models.ForeignKey(Categories, on_delete=models.SET_NULL,  related_name='subcategories',
                                   null=True, blank=True, verbose_name="Kategoriyalar")
    name = models.CharField(max_length=500, blank=True, null=True, verbose_name="Pastgi Kategoriya", db_index=True)
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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                             verbose_name="Foydalanuvchi")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nomi", db_index=True)
    subject = models.TextField(verbose_name="Izoh")
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
    project = models.ForeignKey(Projects, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name="Kategoriya")
    file_code = models.CharField(max_length=25, verbose_name="Fayil Kodi", blank=True, null=True)
    file = models.FileField(upload_to="PDF-file/%Y/%m/%d", verbose_name="FAYL")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return f"Fayil kodi: {self.file_code}"

    class Meta:
        verbose_name = "Fayil"
        verbose_name_plural = "Loyiha Fayillari"



class APIRequestCount(models.Model):
    endpoint = models.CharField(max_length=255, unique=True, verbose_name="So'rov")
    count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Foydalanuvchi')
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP Address")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="So'rov vaqti")
    def __str__(self):
        return f"{self.endpoint} -- {self.count}"

    class Meta:
        verbose_name = "So'rovlar soni"


class APIRequestCountLog(models.Model):
    api_request = models.ForeignKey(APIRequestCount, related_name='logs', on_delete=models.CASCADE,
                                    verbose_name="Oxirgi so'rov")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Oxirgi so'rov vaqti")

    def __str__(self):
        return f"{self.api_request} -- {self.timestamp}"

    class Meta:
        verbose_name = "So'rov vaqtlari"