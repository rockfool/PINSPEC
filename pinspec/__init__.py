import _pinspec
from pinspec import *
import os
import random
import datetime
import signal

# Tell Python to recognize CTRL+C and stop the C++ extension module
# when this is passed in from the keyboard
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Set a default logging level
set_log_level('NORMAL')

# Set a log file name using a date and time
now = datetime.datetime.now()
current_time = str(now.month) + '-' + str(now.day) + '-' + str(now.year) + '--' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
set_log_filename('log/pinspec-' + current_time + '.log');

# Set the path to the xs library to the one that was installed
pkg_path = os.path.dirname(__file__)
xs_lib_path = os.path.join(pkg_path, 'xs-lib/')
setXSLibDirectory(xs_lib_path)

# Restore the cross-section library from backup
restoreXSLibrary()

# Get instances of TallyBank and TallyFactory singleton classes
TallyBank = pinspec.TallyBank.Get()
TallyFactory = pinspec.TallyFactory.Get()
