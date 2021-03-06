# Generated by Django 2.2 on 2020-08-01 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Unknown', max_length=40, verbose_name='Автор')),
                ('email', models.EmailField(default='Unknown', max_length=40, verbose_name='Почта')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('publish_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Время публикации')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='new', max_length=15, verbose_name='Модерация')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
