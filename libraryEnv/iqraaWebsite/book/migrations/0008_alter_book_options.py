# Generated by Django 5.0.6 on 2024-05-17 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_book_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id']},
        ),
    ]
