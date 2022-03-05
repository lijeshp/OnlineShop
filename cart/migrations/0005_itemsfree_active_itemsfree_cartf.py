# Generated by Django 4.0.1 on 2022-01-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_delete_itemspaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsfree',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='itemsfree',
            name='cartF',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist'),
            preserve_default=False,
        ),
    ]
