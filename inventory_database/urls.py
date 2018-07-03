from django.conf.urls import url
from inventory_database import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^search/$', views.search, name='search'),
	url(r'^add_asset/$', views.add_asset, name='add_asset'),
	url(r'^add_employee/$', views.add_employee, name='add_employee'),
	url(r'^add_student/$', views.add_student, name='add_student'),
	url(r'^add_software/$', views.add_software, name='add_software'),
	url(r'^add_lab_classroom/$', views.add_lab_classroom, name='add_lab_classroom'),
	url(r'^asset/(?P<asset_name_slug>[\w\-]+)/$', views.show_asset, name='show_asset'),
	url(r'^employee/(?P<employee_id_slug>[\w\-]+)/$', views.show_employee, name='show_employee'),
	url(r'^room/(?P<room_name_slug>[\w\-]+)/$', views.show_room, name='show_room'),
	url(r'^student_lab/', views.student_lab, name='student_lab'),
	url(r'^faculty_staff/', views.faculty_staff, name='faculty_staff'),
]