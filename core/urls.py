from django.conf.urls import url
from . import views
from core.views import EvidenceView

app_name = 'core'
urlpatterns = [
    # ex: /core/
    url(r'^$', views.index, name='index'),
    # ex: /core/5/
    url(r'^(?P<corecomp_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /core/submitted/
    url(r'^submitted', views.submitted, name='submitted'),
    # ex: /core/CES/
	url(r'^', EvidenceView.as_view(), name='evidence')
]