import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class OTCBase(models.Model):
    code = models.UUIDField(verbose_name='Code', default=uuid.uuid4)
    valid_until = models.DateTimeField(verbose_name='Valid until')
    is_used = models.BooleanField(verbose_name='Was used', default=False)
    used_at = models.DateTimeField(verbose_name='Valid until')
    #TODO: Add meta + abstractmodel:)

    @property
    def is_valid(self):
        return not self.is_used and self.valid_until< datetime.now()

    def apply(self):
        raise NotImplemented


class RegisterOTC(OTCBase):
    new_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def apply(self):
        raise NotImplemented

class ResetPasswordOTC(OTCBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def apply(self, new_passwd):
        raise NotImplemented
