# Generated by Django 3.2.16 on 2022-10-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20221017_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='payment_method',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ManyToManyField(null=True, to='App.Product_details'),
        ),
    ]
