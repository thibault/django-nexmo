# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from libnexmo import Nexmo

from django.conf import settings


def send_message(frm=settings.NEXMO_FROM, to=None, text=None):
    """Shortcut to send a sms using libnexmo api.

    :param frm: The originator of the message
    :param to: The message's recipient
    :param text: The text message body

    Example usage:

    >>> send_message(to='+33123456789', text='My sms message body')

    """
    assert to is not None
    assert text is not None

    nexmo = Nexmo(settings.NEXMO_API_KEY, settings.NEXMO_API_SECRET)
    response = nexmo.send_sms(frm, to, text)
    return response
