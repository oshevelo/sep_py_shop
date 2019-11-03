from django.db import models
from django.contrib.auth.models import User


class MailLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    receiver_email = models.CharField(max_length=500)

    def __str__(self):
        return 'email to {} set at {}'.format(self.receiver_email, self.created_at)
