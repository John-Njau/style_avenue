# Generated by Django 4.1 on 2022-08-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="ordered_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="order",
            name="time",
            field=models.TimeField(),
        ),
    ]
