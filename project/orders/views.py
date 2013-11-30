# -*- coding: utf-8 -*-
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from orders.models import *


class CustomersList(ListView):
    template_name = "order_list.html"
    model = Order


class CustomerDetails(DetailView):
    model = Customer
