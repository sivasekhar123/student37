from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^staff_reg/$', views.staff_reg, name='staff_reg'),
    url(r'^staff_detail/$', views.staff_detail, name='staff_detail'),
    url(r'^staff_info/$', views.staff_info, name='staff_info'),
    url(r'^student_info/$', views.student_info, name='student_info'),
    url(r'^all_staff/$', views.all_staff, name='all_staff'),
    url(r'^all_students/$', views.all_students, name='all_students'),
]
