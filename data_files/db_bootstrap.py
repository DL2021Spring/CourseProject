


import MySQLdb as mdb
import sys

from datetime import datetime

__author__ = 'Daniel'


def start_stamp(func):
  
  def ret(*args):
    print ("%s: exec %s" % (str(datetime.now()), func.__name__))
    return func(*args)

  return ret


class Connection(object):
  def __init__(self, db_name, default_file):
    print "running at db: %s" % (db_name)
    self.con = mdb.connect(read_default_file=default_file, db=db_name)
    
    
