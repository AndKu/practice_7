# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import *
from library.models import *


class BookList(ListView):
    template_name="books.html"
    model = Book


class BookDetail(DetailView):
    template_name = "book.html"
    model = Book


class AuthorList(ListView):
    template_name = "authors.html"
    model = Author


class AuthorDetail(DetailView):
    template_name = "author.html"
    model = Author


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Account created success! Confirm your email.'))
            return redirect("/login/")
        messages.error(request, (u'Please correct the error below.'))
    else:
        form = UserCreationForm()
    return render(request, "registation.html", {
        'form': form,
    })
