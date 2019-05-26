from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^shop/$', views.shoppage, name='shop'),
]
