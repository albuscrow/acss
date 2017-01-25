from ACUser.models import User
from django.utils import timezone
from subprocess import call
from os.path import exists


def get_pid_file_name(user_name):
    return './pid/' + str(user_name)


def get_start_command(user):
    start_command_temple = 'ss-server -s 0.0.0.0' \
                           ' -m chacha20' \
                           ' --fast-open' \
                           ' -6' \
                           ' -u' \
                           ' -A' \
                           ' -p %d' \
                           ' -k %s' \
                           ' -f %s'
    return start_command_temple % (user.port, user.password, get_pid_file_name(user.user_name))


def get_stop_command(user_name):
    return 'kill -9 `cat {0}` && rm {0}' \
        .format(get_pid_file_name(user_name))


def run_command(command):
    with open('log', mode='a') as of:
        of.write(command)
        of.write('\n')
    call(command, shell=True)


def stop_ss_server(user_name):
    if exists(get_pid_file_name(user_name)):
        run_command(get_stop_command(user_name))


def start_ss_server(user):
    if not exists(get_pid_file_name(user.user_name)):
        run_command(get_start_command(user))


def update_ss_server():
    for u in User.objects.all():
        if u.expired_date > timezone.now():
            start_ss_server(u)
        else:
            stop_ss_server(u.user_name)


def stop_all_ss_server():
    for u in User.objects.all():
        stop_ss_server(u.user_name)
