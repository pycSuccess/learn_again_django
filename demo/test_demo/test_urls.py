from django.conf.urls import url
from test_demo.views import test_form
from test_demo import views

urlpatterns = [
    url(r'^form/', test_form, name='test_form'),
    url(r'^add_user/', views.add_user, name='add_user'),
    url(r'^test_paginator/', views.test_paginator, name='test_paginator'),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^get_page/(?P<page>\d*)/', views.get_page_index, name='get_page_index'),
    url(r'^get_page/', views.get_page, name='get_page'),
    url(r'.*', views.test_exception, name='404'),

]