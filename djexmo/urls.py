from django.conf.urls import patterns, url


urlpatterns = patterns(
    'djexmo.views',
    url(r'^callback/$', 'callback', name='nexmo_callback'),
)
