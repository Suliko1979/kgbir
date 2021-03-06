# Generated by Django 2.2 on 2021-09-09 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('text', models.TextField(verbose_name='Текст')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Баннер')),
                ('descritpion', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(default='', unique=True, verbose_name='URL')),
                ('text', models.TextField(default='', verbose_name='Текст')),
                ('header', models.CharField(blank=True, max_length=120, null=True, verbose_name='Заголовок')),
                ('subheader', models.CharField(blank=True, max_length=120, null=True, verbose_name='Подзаголовок')),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('active', models.BooleanField(default=True, verbose_name='Опубюликовать')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('keywords', models.CharField(max_length=120)),
                ('sort', models.PositiveIntegerField(default=0, unique=True, verbose_name='Порядок')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Banner')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.Category', verbose_name='Категория')),
            ],
        ),
    ]
