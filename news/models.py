from tabnanny import verbose
from django.db import models



class Articles(models.Model):
    title= models.CharField('Название',max_length=50)
    anons = models.CharField('Анонс',max_length=250)
    full_text =models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank =True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name