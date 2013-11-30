from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
from library.views import *
from orders.views import *

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', BookList.as_view()),
    url(r'^library/$', BookList.as_view()),
    url(r'^library/books/$', BookList.as_view()),
    url(r'^library/books/(?P<pk>\w+)/$', BookDetail.as_view()),
    url(r'^library/authors/$', AuthorList.as_view()),
    url(r'^library/authors/(?P<pk>\w+)/$', AuthorDetail.as_view()),
    url(r'^orders/$', CustomersList.as_view()),
    url(r'^customers/(?P<pk>\d+)/$', CustomerDetails.as_view(template_name="customer.html")),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^registration/$', registration),
    #url(r'^log/$', 'pages.views.listing'),
    #url(r'^log/(?P<dir_name>\w+)/$', 'pages.views.listing'),

    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
