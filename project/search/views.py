# Create your views here.
from django import forms
from library.models import Book


class SearchBook(forms.Form):
    template_name = "search_book.html"
    model = Book