# Generated by Django 4.1.3 on 2023-07-23 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0005_alter_branch_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
    ]