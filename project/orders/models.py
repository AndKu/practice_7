from django.db import models

# Create your models here.
from library.models import Book


class Customer(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    address = models.TextField()
    email = models.EmailField()
    is_approved = models.BooleanField()

    def __unicode__(self):
        return u'%s %s.' % (self.firstName, self.lastName)


class Order(models.Model):
    itemId = models.ForeignKey(Book)
    created = models.DateField(auto_now_add=True)
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.itemId
