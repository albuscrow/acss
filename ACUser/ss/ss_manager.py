from django.utils import timezone
from .ss_configure import SSConfigure
from json import dumps
from subprocess import call

ss_config_file_path = './server.json'

ss_command_temple = 'ss-server -c ./server.json'
# restart_ss_command = ss_command_temple % 'restart'
# start_ss_command = ss_command_temple % 'start'


def restart_ss():
    # call(restart_ss_command)
    pass


def start_ss():
    # call(start_ss_command)
    pass


def update_ss_config_file():
    from ACUser.models import User
    pps = SSConfigure()
    for u in User.objects.filter(expired_date__gt=timezone.now()):
        pps.add_user(u.port, u.password)

    with open(ss_config_file_path, 'w') as of:
        of.write(pps.to_json())

    restart_ss()
