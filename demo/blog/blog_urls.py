from django.conf.urls import url

from blog import views
urlpatterns = [
    url(r'login/', views.login, name='login'),
    url(r'add/', views.add, name='add'),
    url(r'select/', views.select, name='select'),
]