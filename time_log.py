import logging
import logging.config
import datetime
import threading
import os
import sys

previous_map = {"": datetime.datetime.now()}

if not os.path.exists("logs/"):
    print(os.makedirs("logs/"))
logging.config.fileConfig('logging.conf')
console_log = logging.getLogger('console')
time_log_log = logging.getLogger('time')


class DualLogger(object):
    def __init__(self):
        self.terminal = sys.stdout

    def write(self, message):
        self.terminal.write(message)
        console_log.debug(message)

    def flush(self):
        self.terminal.flush()
    
    def console(self, message):
        self.terminal.write(message)

class ErrLogger(object):
    def __init__(self):
        self.terminal = sys.stderr

    def write(self, message):
        self.terminal.write(message)
        console_log.error(message)

    def flush(self):
        self.terminal.flush()
        

sys.stdout = DualLogger()
sys.stderr = ErrLogger()

def time_log(s):
    return time_key(s, str(threading.get_ident()))

def time_key(s, key):
    if key is None:
        key = ""
    now = datetime.datetime.now()
    previous_log = previous_map.get(key, now)
    elapse = now - previous_log
    previous_map[key] = now
    message = "{}::{}---{}--{}\n".format(now.strftime('%Y-%m-%d %H:%M:%S.%f'),
                threading.get_ident(), elapse, s)
    sys.stdout.console(message)
    time_log_log.info("{}--{}".format(elapse, s))
    
