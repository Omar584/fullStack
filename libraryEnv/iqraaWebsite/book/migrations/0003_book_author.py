# Generated by Django 5.0.6 on 2024-05-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]
