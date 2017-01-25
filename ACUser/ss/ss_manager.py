from ACUser.models import User
from django.utils import timezone
from subprocess import call


def get_pid_file_name(user_name):
    return './pid/' + str(user_name)


def get_start_command(user):
    start_command_temple = 'ss-server -s 0.0.0.0' \
                           '-m chacha20' \
                           '--fast-open' \
                           '-6' \
                           '-u' \
                           '-A' \
                           '-p %d' \
                           '-k %s' \
                           '-f %s'
    return start_command_temple % (user.port, user.password, get_pid_file_name(user.user_name))


def get_stop_command(user):
    stop_command_temple = 'kill -9 `cat {0}` && rm {0}'.format(get_pid_file_name(user.user_name))


def run_command(command):
    call(command, shell=True)


def update_ss_server():
    for u in User.objects.filter(expired_date__gt=timezone.now()):
        if u.expired_date > timezone.now():
            run_command(get_start_command(u))
        else:
            run_command(get_stop_command(u))
