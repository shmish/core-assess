from django.conf.urls import url
from . import views
from classroom.views import create_classroom_view, delete_block_view, randomize

app_name = "classroom"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submitted', views.submitted, name='submitted'),
	url(r'^classup/$', create_classroom_view, name='classroom'),
    url(r'^block/$', views.block, name='block'),
    # url(r'^(?P<pk>[0-9]+)/deleteblock/$', delete_block_view, name='deleteblock'),
    url(r'^(?P<pk>[0-9]+)/deleteblock/$', delete_block_view, name='deleteblock'),
    url(r'^adjust/$', views.adjust, name='adjust'),
    url(r'^random/$', views.block, name='random'),
]