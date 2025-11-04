from django.db import models

class Books(models.Model):

    GENRE = (
         ('роман', 'роман'),
         ('драма', 'драма'),
         ('лирика' ,'лирика' ),
         ('эпос' ,'эпос' )
    )

    title = models.CharField(max_length=100, verbose_name='введение название книги')
    image = models.ImageField(upload_to='books/', verbose_name='загрузите фото')
    description = models.TextField(verbose_name='укажиете описание')
    author = models.CharField (max_length=100, verbose_name='укажиет автора', default = 'Ivenov Ivan')
    genre = models.CharField(max_length=100, choices= GENRE, verbose_name='роман')
    country = models.CharField(max_length=100, default='США', verbose_name='укажите страну')
    duration = models.PositiveIntegerField(verbose_name='количество страниц', default='100000')
    video = models.URLField(verbose_name='ссылка на обзор')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)



    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'book'