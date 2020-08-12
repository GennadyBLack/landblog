from django.db import models
from django.urls import reverse
class Article(models.Model):

    

    title = models.CharField(max_length=500, verbose_name='Название поста')
    body = models.TextField(verbose_name='Текст поста')
    description = models.TextField('Description',max_length=500,null=True)
    poster = models.ImageField('Постер',upload_to='articles/',null=True)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
    def __str__(self):
        return '({0}) Пост: {1}, от {2}'.format(self.id, self.title, self.date_created.strftime('%d-%m-%y %H:%M'))


    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"id":self.id})
