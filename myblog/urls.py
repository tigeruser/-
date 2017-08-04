from django.conf.urls import include, url
from views import index,show,edit,editAction,change,changeAction

urlpatterns = [
    url(r'^index/',index),
    url(r'^show/(?P<id>[0-9]+)',show,name='show'),
    url(r'^edit/',edit, name='edit'),
    url(r'^editAction/',editAction,name='editAction'),
    url(r'^changeq/(?P<id>[0-9]+)',change, name='change'),
    url(r'^changeAction/(?P<id>[0-9]+)', changeAction, name='changeAction')
]
