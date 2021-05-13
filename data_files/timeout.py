import signal
__author__ = 'Daniel'



def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(10)   
try:
    while True:
        pass
except Exception, msg:
    print "Timed out!"

signal.alarm(0)   