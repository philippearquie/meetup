from django.conf.urls import patterns, url
from Meetup import views

urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'),
                       url(r'^employees/$',views.employee_table, name='employee'),
                       url(r'^companies/$',views.company_table, name='company'))
