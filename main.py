""" Uses terminal-notifier to display an OSX notification after a set time """

import sys
import subprocess
from threading import Timer

INPUT_TEXT = sys.argv[1]
INPUT_TIME = int(sys.argv[2])


def output_notification():
    bash_command = '/usr/local/bin/terminal-notifier -title \'ALERT\' -message \'%s\'' % (INPUT_TEXT)
    subprocess.check_output(['bash', '-c', bash_command])


NOTIFICATION_TIMER = Timer(INPUT_TIME, output_notification)

NOTIFICATION_TIMER.start()
