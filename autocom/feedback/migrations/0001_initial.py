# Generated by Django 2.2 on 2021-09-12 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(max_length=18)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('call_time', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Данные клиента',
            },
        ),
    ]
