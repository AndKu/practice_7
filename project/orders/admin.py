# -*- coding: utf-8 -*-


from django.contrib import admin
from orders.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['itemId', 'created', 'customer']
    ordering = ['created']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'address', 'email']


admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
