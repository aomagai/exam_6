# Generated by Django 2.2 on 2020-08-01 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200801_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='email',
            field=models.EmailField(max_length=40, verbose_name='Почта'),
        ),
    ]