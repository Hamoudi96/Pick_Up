from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^health', views.health, name='health'),
               url(r'^404', views.handler404, name='404'),
               url(r'^500', views.handler500, name='500'),
               url(r'^register', views.register, name='register'),
               url(r'^profile', views.profile, name='profile'),
               url(r'^teamCreate', views.create_team, name='createTeam'),
               url(r'^joinTeam', views.join_team, name='joinTeam'),
               url(r'^fieldLoaction', views.field_location, name='fieldLocation'),
               url(r'^createField', views.create_field, name='fieldCreate'),
               url(r'^logout', views.logout, name='logout')
               ]
