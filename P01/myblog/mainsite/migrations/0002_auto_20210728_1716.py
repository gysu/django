# Generated by Django 3.2.5 on 2021-07-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='abstract',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pic_url',
            field=models.URLField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
