# Generated by Django 4.2.14 on 2024-08-31 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APIRequestCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=255, unique=True, verbose_name="So'rov")),
                ('count', models.IntegerField(default=0)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="So'rov vaqti")),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': "So'rovlar soni",
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='Nomi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan vaqti')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='Pastgi Kategoriya')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan vaqti')),
                ('categories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='db_main.categories', verbose_name='Kategoriyalar')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_main.subcategories', verbose_name='Pastgi Kategoriyalar bolalari')),
            ],
            options={
                'verbose_name': 'Pastgi Kategoriya',
                'verbose_name_plural': 'Pastgi Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Nomi')),
                ('subject', models.TextField(verbose_name='Izoh')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan vaqti')),
                ('subcategories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_main.subcategories', verbose_name='Pastgi Kategoriyalar')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Loyiha',
                'verbose_name_plural': 'Loyihalar',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_code', models.CharField(blank=True, max_length=25, null=True, verbose_name='Fayil Kodi')),
                ('file', models.FileField(upload_to='file', verbose_name='Fayl')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan vaqti')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='db_main.projects', verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name': 'Fayil',
                'verbose_name_plural': 'Loyiha Fayillari',
            },
        ),
        migrations.CreateModel(
            name='APIRequestCountLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name="Oxirgi so'rov vaqti")),
                ('api_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='db_main.apirequestcount', verbose_name="Oxirgi so'rov")),
            ],
            options={
                'verbose_name': "So'rov vaqtlari",
            },
        ),
    ]
