from django.utils.translation import ugettext as _


NEXMO_STATUSES = {
    "delivered": _("Message arrived to handset."),
    "expired": _("Message timed out after we waited 48h to receive status from mobile operator."),
    "failed": _("Message failed to be delivered."),
    "accepted": _("Message has been accepted by the mobile operator."),
    "submitted": _("Message has been accepted by the mobile operator."),
    "buffered": _("Message is being delivered."),
    "unknown": _("Un documented status from the mobile operator."),
}

UNKNOWN_STATUS = _('Unknown status')


NEXMO_MESSAGES = {
    0: _('Delivered'),
    1: _('Unknown error'),
    2: _('Absent Subscriber - Temporary'),
    3: _('Absent Subscriber - Permenant'),
    4: _('Call barred by user'),
    5: _('Portability Error'),
    6: _('Anti-Spam Rejection'),
    7: _('Handset Busy'),
    8: _('Network Error'),
    9: _('Illegal Number'),
    10: _('Invalid Message'),
    11: _('Unroutable'),
    99: _('General Error'),
}

UNKNOWN_MESSAGE = _('Unknown error')
