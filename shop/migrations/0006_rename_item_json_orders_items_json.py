# Generated by Django 4.1.3 on 2022-12-11 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_delete_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='item_json',
            new_name='items_json',
        ),
    ]