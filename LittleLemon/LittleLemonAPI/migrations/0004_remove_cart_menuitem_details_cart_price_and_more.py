# Generated by Django 4.1.7 on 2023-02-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0003_cart_menuitem_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='menuitem_details',
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True, db_index=True),
        ),
    ]
