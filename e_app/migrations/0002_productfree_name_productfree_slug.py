# Generated by Django 4.0.1 on 2022-01-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfree',
            name='name',
            field=models.CharField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productfree',
            name='slug',
            field=models.SlugField(default=0, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
