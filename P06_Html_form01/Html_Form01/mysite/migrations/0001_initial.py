# Generated by Django 3.2.6 on 2021-08-20 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='請輸入暱稱', max_length=50)),
                ('message', models.TextField()),
                ('del_pass', models.CharField(max_length=50)),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField(default=False)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.mood')),
            ],
        ),
    ]