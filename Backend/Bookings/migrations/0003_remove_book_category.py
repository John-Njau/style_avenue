# Generated by Django 4.1 on 2022-09-05 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Bookings", "0002_alter_book_date_alter_book_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="category",
        ),
    ]
