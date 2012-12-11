from django.conf.urls import patterns, include, url
from docView import views
from fileuploader import views as fview
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^docViewer/$', views.docViewer),
	(r'^docViewer/confirmation/$', views.confirmation),
	(r'^fileuploader/$', fview.fileuploader),
        (r'^registerit/$', views.register),
        (r'^testtemplate/$', views.test_login),
        (r'^accounts/login/$', login),
        (r'^accounts/logout/$', logout),
        (r'^accounts/profile/$', views.projects),
        (r'^accounts/profile/create_project/$', views.create_project),
        # Examples:
    # url(r'^$', 'diascriptr.views.home', name='home'),
    # url(r'^diascriptr/', include('diascriptr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
