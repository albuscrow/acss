from django.db import models
from django.utils import timezone
import socket


class User(models.Model):
    user_name = models.CharField(max_length=64)
    port = models.IntegerField()
    password = models.CharField(max_length=64)
    expired_date = models.DateTimeField()

    @staticmethod
    def get_available_port():
        s = socket.socket()
        s.bind(('', 0))
        return s.getsockname()[1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port = self.get_available_port()

    def __str__(self):
        return str(self.user_name) \
               + ' ' + str(self.port) \
               + ' ' + str(self.expired_date)

    def is_expired(self):
        return timezone.now() > self.expired_date

    is_expired.admin_order_field = 'expired_date'
    is_expired.boolean = True
    is_expired.short_description = 'is expired'
