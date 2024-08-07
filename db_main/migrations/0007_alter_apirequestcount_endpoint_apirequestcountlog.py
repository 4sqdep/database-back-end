# Generated by Django 4.2.14 on 2024-08-09 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_main', '0006_apirequestcount_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apirequestcount',
            name='endpoint',
            field=models.CharField(max_length=255, unique=True, verbose_name="So'rov"),
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
