from django.conf.urls import patterns, url


urlpatterns = patterns(
    'nexmo.views',
    url(r'^callback/$', 'callback', name='nexmo_callback'),
)
