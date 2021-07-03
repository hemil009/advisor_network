from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
     url(r'^register/$', views.register_view, name="register"),
     url(r'^login/$', views.login_view, name="login"),
     # url(r"^(?P<user-id>\d+)/advisor", views.list_view, name='list'),
     # url(r"^(?P<user-id>\d+)/advisor/(?P<user-id>\d+)", views.booking_view, name='booking'),
     # url(r"^(?P<user-id>\d+)/booking", views.booked_view, name='booked')
]
