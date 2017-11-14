from django.conf.urls import include, url
#from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^basicview/', include('calc.urls')),
	url(r'^auth/', include('loginsys.urls')),
	url(r'^', include('calc.urls')),
]
