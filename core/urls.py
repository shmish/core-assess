from django.conf.urls import url
from . import views
from core.views import list_evidence_view, create_evidence_view, list_submissions_view

app_name = 'core'
urlpatterns = [
    # ex: /core/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<corecomp_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^submitted', views.submitted, name='submitted'),
	url(r'^evidence_form/$', create_evidence_view, name='evidence'),
	url(r'^CES/$', list_evidence_view, name='CES'),
    url(r'^submissions/$', list_submissions_view, name='submissions')
]