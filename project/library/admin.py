# -*- coding: utf-8 -*-


from django.contrib import admin
from library.models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'birthyear']
    list_display_links = ['last_name', 'first_name']
    ordering = ['last_name', 'first_name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'publication_date']
    list_display_links = ['title']
    search_fields = ['title']
    ordering =['publication_date']
    fieldsets = (
        (None, {'fields': ('title', 'authors', 'publication_date', 'description')}),
        ('Выходные данные', {
            'classes': ('wide',),
            'fields': ('publisher',),
        }),
    )


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['title', 'country', 'city']
    list_display_links = ['title']
    ordering = ['title']
    list_filter = ['country', 'city']
    fieldsets = (
        (None, {'fields': ('title', )}),
        ('Контактная информация', {
            'classes': ('wide',),
            'fields': ('country', 'city', 'address', 'website',),
        }),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
