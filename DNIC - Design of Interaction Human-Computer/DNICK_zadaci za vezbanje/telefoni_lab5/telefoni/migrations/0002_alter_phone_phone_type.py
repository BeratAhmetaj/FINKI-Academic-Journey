# Generated by Django 4.1 on 2024-06-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telefoni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_type',
            field=models.CharField(choices=[('small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=15),
        ),
    ]