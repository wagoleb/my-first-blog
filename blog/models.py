from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class userzy(models.Model):
    nr = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {}.{}'.format(self.nr, self.imie[:3], self.nazwisko[:3])
