# Generated by Django 4.1.3 on 2023-07-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pr_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
