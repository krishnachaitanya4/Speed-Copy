# Generated by Django 4.1.3 on 2023-01-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_orderdetails_sides'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='status',
            field=models.TextField(default='Pending', max_length=10),
            preserve_default=False,
        ),
    ]
