from django.conf.urls import url

from blog import views
urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^add/', views.add, name='add'),
    url(r'select/', views.select, name='select'),
    url(r'include/', views.test_include, name='test_include'),
    url(r'extends/', views.test_extends, name='test_extends'),
    url(r'many_toadd/', views.many_to, name='many_to'),
    url(r'test_annotate/', views.test_annotate, name='test_annotate'),
    url(r'^test_son/', views.test_son_select, name='test_son'),
    url(r'^test_manytomany', views.test_manytomany, name='test_manytomany'),
    url(r'^test_onetoone/', views.test_onetoone, name='test_onetoone'),
    url(r'^test_jointable/', views.test_jointable, name='test_jointable'),
    url(r'^index/', views.index, name='index'),
    url(r'^test_ajax/', views.test_ajax, name='test_ajax'),
    url(r'^get_date/', views.get_date, name='get_date'),
    url(r'^session_login/', views.test_session_login, name='session_login'),
    url(r'^session_index/', views.test_session_index, name='session_index'),

]