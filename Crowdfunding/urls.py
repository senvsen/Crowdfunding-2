from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
import xadmin
xadmin.autodiscover()
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Crowdfunding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('qdinvest.urls')),
    url(r'^c/', include('qdinvest.urls')),
    url(r'^app/', include('qdinvest.urlsapp')),
    url(r'^w/', include('qdinvest.urlsWeChat')),
    url(r'admin/', include(xadmin.site.urls)),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^c/stock/', include('qdinvest.urls')),
    url(r'^c/bond/', include('qdinvest.urls')),

)


if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}),)