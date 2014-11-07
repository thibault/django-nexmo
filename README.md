django-nexmo
============

[![Build
Status](https://travis-ci.org/thibault/django-nexmo.svg)](https://travis-ci.org/thibault/django-nexmo)

`django-nexmo` is a tiny Django app to send sms [using the Nexmo
provider](https://www.nexmo.com/). The actual communication with Nexmo's API is
[delegated to libnexmo](https://github.com/thibault/libnexmo).

Installation
------------

Installation using pip is simple:

    $ pip install django-nexmo

Add the `nexmo` app to your installed applications:

```python
INSTALLED_APPS = (
    …
    'nexmo',
    …
)
```

Configuration
-------------

You need to add a few lines in your `settings.py` file for django-nexmo to work:

```python
NEXMO_API_KEY = 'API_KEY'
NEXMO_API_SECRET = 'SECRET'
NEXMO_DEFAULT_FROM = 'Name or phone'
```


Did I mention that you need a [Nexmo account](https://www.nexmo.com/)?
Seems quite obvious to me.

You can get your API_KEY and SECRET from your [Nexmo
Dashboard](https://dashboard.nexmo.com/private/dashboard)

Basic usage
-----------

The `nexmo` apps gives you access to a shortcut to send text messages easily.

```python
from nexmo import send_message
send_message(frm='+33123456789', to='+33612345678', message='My sms message body')
```

The `frm` parameter can be omited. In that case, the `NEXMO_FROM` configuration
field will be used instead.

```python
from nexmo import send_message
send_message(to='+33612345678', message='My sms message body')
```

Advanced usage
--------------

`django-nexmo` uses [libnexmo](https://github.com/thibault/libnexmo).
Therefore, you can [use the library for a low level access to the Nexmo
API](http://libnexmo.readthedocs.org/en/latest/).



Handling callbacks
------------------

Nexmo can call one of your urls to send further details about a text message processing.

`django-nexmo` provides a very basic callback handler that does nothing but logging
Nexmo calls.

In your main `urls.py` file:

```python
urlpatterns = patterns('',
    …
    url(r'^nexmo/', include('nexmo.urls')),
    …
)
```

This will declare a callback view accessible through the
`http://your-site.url/nexmo/callback/` url.

Copy this url and paste it in the "Callback URL" section of your "API settings"
section of your Nexmo.com account.

Testing
-------

`django-nexmo` uses [tox for testing in multiple
environments](https://pypi.python.org/pypi/tox).

To run the tests, create a new virtualenv, then `pip install tox`. To run the
tests:

    tox

Credits
-------

Crafted with love by [Thibault Jouannic](http://www.miximum.fr). Available for
[Python / Django Freelancing](http://www.miximum.fr/a-propos/).
