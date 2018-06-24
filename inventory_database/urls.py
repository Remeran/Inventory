from django.conf.urls import url
from inventory_database import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
	url(r'^search/$', views.search, name='search'),
    url(r'^add_asset/$', views.add_asset, name='add_asset'),
    #url(r'^asset/(?P<asset_name_slug>[\w\-]+)/$', views.show_asset, name='show_asset'),
]