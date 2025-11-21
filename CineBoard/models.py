from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )

class Film(models.Model):
    GENRE_CHOICES = [
        ('драма', 'Драма'),
        ('комедия', 'Комедия'),
        ('боевик', 'Боевик'),
        ('ужасы', 'Ужасы'),
        ('фантастика', 'Фантастика'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    release_date = models.DateField()
    rating = models.IntegerField()
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.title
