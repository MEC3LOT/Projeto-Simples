# Generated by Django 5.0.7 on 2024-07-24 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]
