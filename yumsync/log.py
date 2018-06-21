import os
import sys
import time

start = int(time.time())

def log(msg, header=False, log_dir=None, force=False):
    time_str = time.strftime('%Y-%m-%dT%X%z')
    delta = int(time.time()) - start
    minute, second = divmod(delta, 60)
    hour, minute = divmod(minute, 60)
    delta_str = '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, second)

    output_str = "==> %s" % msg if header else msg

    if log_dir is not None:
        if os.path.exists(log_dir):
            with open(os.path.join(log_dir, 'sync.log'), 'a') as logfile:
                logfile.write('{0} {1}\n'.format(time_str, output_str))

    if force or not sys.__stdout__.isatty():
        sys.__stdout__.write('{0} {1}\n'.format(delta_str, output_str))
        sys.__stdout__.flush()
