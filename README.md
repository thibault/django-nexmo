# django-nexmo

`django-nexmo` is a tiny Django app to send sms using the Nexmo provider.

## Installation

Installation using pip is simple:

    $ pip install django-nexmo

Add the `nexmo` app to your installed applications:

    INSTALLED_APPS = (
        …
        'nexmo',
        …
    )

## Configuration

You need to add a few lines in your `settings.py` file for django-nexmo to work:

    NEXMO_USERNAME = 'username'
    NEXMO_PASSWORD = 'password'
    NEXMO_FROM = 'Name or phone'

Did I mention that you need a [Nexmo account](https://www.nexmo.com/)?
Seems quite obvious to me.


## Basic usage

The `nexmo` apps gives you access to a shortcut to send text messages easily.

    from nexmo import send_message
    send_message('+33612345678', 'My sms message body')

Is that all? Yes… for now.


## Advanced usage

`django-nexmo` embeds [libpynexmo by Marco Londero](https://github.com/marcuz/libpynexmo).
Therefore, you can import and use the `NexmoMessage` class to manually forge
requests to the Nexmo API.

    from nexmo.libpynexmo.nexmomessage import NexmoMessage


    params = {
        'api_key': settings.NEXMO_USERNAME,
        'api_secret': settings.NEXMO_PASSWORD,
        'type': 'unicode',
        'from': settings.NEXMO_FROM,
        'to': to,
        'text': message.encode('utf-8'),
    }
    sms = NexmoMessage(params)
    response = sms.send_request()


## Handling callbacks

Nexmo can call one of your urls to send further details about a text message processing.

`django-nexmo` provides a very basic callback handler that does nothing but logging
Nexmo calls.

In your main `urls.py` file:

    urlpatterns = patterns('',
        …
        url(r'^nexmo/', include('nexmo.urls')),
        …
    )

This will declare a callback view accessible through the
http://your-site.url/nexmo/callback/ url.

Copy this url and paste it in the "Callback URL" section of your "API settings"
section of your Nexmo.com account.
