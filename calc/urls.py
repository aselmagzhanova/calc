'''
from django.conf.urls import url, patterns
#from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^1/', 'calc.views.basic_one'),
                       url(r'^2/', 'calc.views.template_two'),
                       url(r'^3/', 'calc.views.template_three_simple'),


                       )
				   
					   
'''


from django.conf.urls import url
from django.contrib import admin
from calc.views import template_three_simple, graphs

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^basicview/3', template_three_simple),
    url(r'^', graphs),

]