# Generated by Django 4.1 on 2024-06-07 11:36

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
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=50)),
                ('manufacturer_location', models.CharField(max_length=50)),
                ('manufacturer_description', models.CharField(max_length=50)),
                ('manufacturer_date', models.DateField()),
                ('is_eu', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_model', models.CharField(max_length=60)),
                ('phone_type', models.CharField(max_length=15)),
                ('phone_image', models.CharField(max_length=250)),
                ('phone_price', models.IntegerField()),
                ('phone_year', models.IntegerField()),
                ('is_new', models.BooleanField()),
                ('phone_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telefoni.manufacturer')),
                ('phone_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
