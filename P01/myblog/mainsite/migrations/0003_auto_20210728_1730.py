# Generated by Django 3.2.5 on 2021-07-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20210728_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pic_url',
        ),
        migrations.AddField(
            model_name='post',
            name='abstracts',
            field=models.TextField(default='待編輯', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pic_urls',
            field=models.URLField(default='https://tw.portal-pokemon.com/play/resources/pokedex/img/pm/224892b2e43c31d5666f73bc6116d0e5719293d2.png', max_length=250),
            preserve_default=False,
        ),
    ]
