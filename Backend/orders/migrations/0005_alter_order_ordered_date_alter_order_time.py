# Generated by Django 4.1 on 2022-08-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_alter_order_quantity_alter_orderitem_quantity"),
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
