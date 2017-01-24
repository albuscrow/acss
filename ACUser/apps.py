from django.apps import AppConfig
from ACUser.ss.ss_manager import start_ss


class ACUserConfig(AppConfig):
    name = 'ACUser'

    def ready(self):
        start_ss()
