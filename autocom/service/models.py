from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('Название', max_length=250)
    slug = models.SlugField('URL', unique=True)
    text = models.TextField('Текст')
    banner = models.ImageField('Баннер', upload_to='images/', blank=True, null=True)
    title = models.CharField('Название', default='', max_length=250)
    descritpion = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_category', kwargs={'slug':self.slug})

    class Meta:
        verbose_name_plural = 'Категории'


class Model(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    name = models.CharField('Название', max_length=250)
    slug = models.SlugField('URL', unique=True, default='')
    text = models.TextField('Текст', default='')
    header = models.CharField('Заголовок', max_length=120, blank=True, null=True)
    subheader = models.CharField('Подзаголовок', max_length=120, blank=True, null=True)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    active = models.BooleanField('Опубликовано', default=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    keywords = models.CharField(max_length=120)
    sort = models.PositiveIntegerField("Порядок", default=0, unique=True)
    banner = models.ImageField('Banner', upload_to='images/', blank=True, null=True)
    price = models.SmallIntegerField(default='0')

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('service_model_view', kwargs={'category':self.category.slug, 'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Товары'
