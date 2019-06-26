from django.conf.urls import url
from test_demo.views import test_form

urlpatterns = [
    url(r'^form/', test_form, name='test_form'),

]