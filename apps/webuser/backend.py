import logging

from django.contrib.auth import backends

from webuser import user_utils
from webuser.user_utils import validate_signature

from raven.contrib.django.raven_compat.models import client

logger = logging.getLogger('user')


class WebUserBackend(backends.ModelBackend):
    def authenticate(self, msg=None, to_sign=None, sig=None, pubkey=None, name=None, source=None):
        try:
            msg = user_utils.sign_data_for_desktop(msg, to_sign)
            valid = validate_signature(msg=msg, sig=sig, pubkey=pubkey)
            logger.info('name:%s, source:%s, msg:%s, key:%s, sig:%s, valid:%s' % (name, source, msg, pubkey, sig, valid))
            if valid:
                # valid success
                # you should return current user
                return None
        except BaseException as e:
            client.captureException()

        return None
