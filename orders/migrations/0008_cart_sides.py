# Generated by Django 4.1.2 on 2022-11-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_orderdetails_colour_orderdetails_pages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sides',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
