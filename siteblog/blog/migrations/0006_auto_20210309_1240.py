# Generated by Django 3.1.1 on 2021-03-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_context'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Record_time',
        ),
        migrations.AlterField(
            model_name='context',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Наименование категории'),
        ),
    ]
