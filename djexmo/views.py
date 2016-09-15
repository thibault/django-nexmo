import logging

from django.http import HttpResponse

from .error_messages import (NEXMO_STATUSES, UNKNOWN_STATUS,
                             NEXMO_MESSAGES, UNKNOWN_MESSAGE)


logger = logging.getLogger(__name__)


def callback(request):
    """Callback URL for Nexmo."""
    message_id = request.GET.get('messageId')
    status_id = request.GET.get('status')
    status_msg = NEXMO_STATUSES.get(status_id, UNKNOWN_STATUS)
    error_id = int(request.GET.get('err-code'))
    error_msg = NEXMO_MESSAGES.get(error_id, UNKNOWN_MESSAGE)

    logger.info(u'Nexmo callback: Sms = %s, Status = %s, message = %s' % (
        message_id,
        status_msg,
        error_msg
    ))

    # Nexmo expects a 200 response code
    return HttpResponse('')
