# ~*~ coding: utf-8 ~*~


from django.db import models
import datetime


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(blank=True, null=True)
    birthyear = models.IntegerField(null=True, blank=True)

    def year(self):
        if self.birthyear:
            return self.birthyear
        else:
            return 'возраст неизвестен'

    def get_absolute_url(self):
        return "/library/authors/%i" % self.id

    def __unicode__(self):
        return u'%s %s.' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField('Название', max_length=128)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())
    description = models.TextField(null=False, blank=False, default="")

    def get_absolute_url(self):
        return "/library/books/%i" % self.id

    def __unicode__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField('Название', max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField('Адрес сайта')

    def __unicode__(self):
        return self.title
