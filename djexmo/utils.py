# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import nexmo

from django.conf import settings


def send_message(frm=None, to=None, text=None):
    """Shortcut to send a sms using libnexmo api.

    :param frm: The originator of the message
    :param to: The message's recipient
    :param text: The text message body

    Example usage:

    >>> send_message(to='+33123456789', text='My sms message body')

    """
    assert to is not None
    assert text is not None

    if frm is None:
        frm = settings.NEXMO_DEFAULT_FROM

    client = nexmo.Client(key=settings.NEXMO_API_KEY, secret=settings.NEXMO_API_SECRET)
    response = client.send_message({
        'from': frm,
        'to': to,
        'text': text
    })
    return response
