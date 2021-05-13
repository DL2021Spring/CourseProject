import sys
import os

import numpy as np
from PIL import Image
import re

__author__ = 'Danyang'


def read_images(path, sz=None):
    
    c = 0
    X, y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    if not re.search(r"\.pgm$|\.jpg$", filename):
                        continue
                    if re.search(r"P00_Ambient\.pgm", filename):  
                        continue
                    im = Image.open(os.path.join(subject_path, filename))
                    im = im.convert("L")
                    
                    if sz is not None:
                        im = im.resize(sz, Image.ANTIALIAS)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            c += 1
    return [X, y]