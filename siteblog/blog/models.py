from django.db import models
from django.urls import reverse_lazy, reverse


class Useful_link(models.Model):
    title = models.CharField(max_length=255, verbose_name='Описание')
    slug = models.CharField(max_length=255,verbose_name="Url", unique=True)
    logotype = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Логотип ссылки')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Добавлена')
    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Полезные ссылки'
        verbose_name_plural = 'Полезные ссылки'


class Context(models.Model):
    title = models.CharField(max_length=255, verbose_name='Действие')
    content = models.TextField(verbose_name='Список документов')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,null=True, verbose_name="Наименование категории")

    def get_absolute_url(self):
        return reverse('actions', kwargs={"pk":self.pk})

    def __str__(self):
        return self.title



    class Meta:
        verbose_name= 'Действие'
        verbose_name_plural = "Действия"


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория документа', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural = "Категории"


