# Generated by Django 4.2.14 on 2024-08-09 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_main', '0004_remove_files_user_remove_projects_files_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIRequestCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint', models.CharField(max_length=255, unique=True, verbose_name="Oxirgi so'rov")),
                ('count', models.CharField(default=0)),
            ],
            options={
                'verbose_name': "So'rovlar soni",
            },
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='db_main.categories', verbose_name='Kategoriyalar'),
        ),
    ]