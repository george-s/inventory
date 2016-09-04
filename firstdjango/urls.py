from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from Inventory import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()

