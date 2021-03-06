# Generated by Django 3.1.1 on 2020-09-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200924_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя клиента')),
                ('email', models.EmailField(max_length=150, verbose_name='E-Mail')),
                ('telephone', models.IntegerField(verbose_name='Телефон')),
                ('data', models.DateField(verbose_name='Дата записи')),
                ('time', models.TimeField(verbose_name='Время записи')),
            ],
        ),
    ]
