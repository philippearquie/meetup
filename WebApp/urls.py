from django.conf.urls import patterns, url, include
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',url(r'^meetup/', include('Meetup.urls',namespace='meetup')))
    # Examples:
    # url(r'^$', 'WebApp.views.home', name='home'),
    # url(r'^WebApp/', include('WebApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
