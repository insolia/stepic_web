from django.conf.urls import include, url
from django.contrib import admin
from qa.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/(?P<q_id>[0-9]+)/', test),
    url(r'^ask/', test),
    url(r'^popular/$', test),
    url(r'^new/$', test),
    url(r'^$', test)
    

]
