# Generated by Django 3.2.5 on 2021-08-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]