from django.conf.urls import patterns, include, url
from docView import views
from fileuploader import views as fview
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf import settings

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






#urlpatterns += patterns('',(r'^page_docs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
        
        # Examples:
    # url(r'^$', 'diascriptr.views.home', name='home'),
    # url(r'^diascriptr/', include('diascriptr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
        # static files (images, css, javascript, etc.)
            urlpatterns += patterns('',
                            (r'^page_docs/(?P<path>.*)$', 'django.views.static.serve', {
                                        'document_root': settings.MEDIA_ROOT}))
