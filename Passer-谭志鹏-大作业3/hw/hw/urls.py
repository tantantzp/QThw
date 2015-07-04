from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hw.views.home', name='home'),
    # url(r'^hw/', include('hw.foo.urls')),
                       
    url(r'^$', 'hw.hw.index'),
    url(r'^hw/$', 'hw.hw.indexhw'),
    url(r'^time/$','hw.time.current_datetime'),
    url(r'^time/plus/(\d{1,2})/','hw.time.hours_ahead'),
    url(r'^hw/formsubmit/$','hw.reply.index'),
    url(r'^static/(?P<path>.*)$',  'django.views.static.serve',  {'document_root': settings.STATIC_ROOT}),
    url(r'^hw/add/','hw.add.index'),
    url(r'^list/','hw.list.index'),
    url(r'^cr/$','hw.caculator_result.index'),
    url(r'^search/$','hw.project3_2.index'),

    url(r'^text3/$','hw.text33.index'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
