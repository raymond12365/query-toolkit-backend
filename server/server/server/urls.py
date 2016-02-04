"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns
from django.contrib import admin

urlpatterns = patterns('queryserver.views',
    url(r'^query/$', 'query_list'),
    url(r'^session/$', 'session_list'),
    url(r'^soc/$', 'soc_list'),
    url(r'^video/$', 'video_list'),
    url(r'^object/$', 'object_list'),
    url(r'^box/$', 'box_list'),
    url(r'^session/(?P<pk>[0-9]+)/$', 'session_detail'),
    url(r'^soc/(?P<pk>[0-9]+)/$', 'soc_detail'),
    url(r'^video/(?P<pk>[0-9]+)/$', 'video_detail'),
    url(r'^query/(?P<pk>[0-9]+)/$', 'query_detail'),
    url(r'^object/(?P<pk>[0-9]+)/$', 'object_detail'),
    url(r'^box/(?P<pk>[0-9]+)/$', 'box_detail'),
    url(r'^querieswithsessionid/(?P<sessionid>[0-9]+)/$', 'queries_with_sessionid'),
    url(r'^videoswithsocid/(?P<socid>[0-9]+)/$', 'videos_with_socid'),
    url(r'^updatepredicates/(?P<queryid>[0-9]+)/$', 'update_predicates_with_queryid'),
    url(r'^updateanswer/(?P<queryid>[0-9]+)/$', 'update_answer_with_queryid'),
    url(r'^updatecomment/(?P<queryid>[0-9]+)/$', 'update_comment_with_queryid'),
    url(r'^updateboxinfo/(?P<boxid>[0-9]+)/$', 'update_boxinfo_with_boxid'),
)
