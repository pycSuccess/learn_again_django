from django.conf.urls import url

from blog import views
urlpatterns = [
    url(r'login/', views.login, name='login'),
    url(r'^add/', views.add, name='add'),
    url(r'select/', views.select, name='select'),
    url(r'include/', views.test_include, name='test_include'),
    url(r'extends/', views.test_extends, name='test_extends'),
    url(r'many_toadd/', views.many_to, name='many_to'),
    url(r'test_annotate/', views.test_annotate, name='test_annotate')
]