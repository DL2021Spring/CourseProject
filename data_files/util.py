
import os
from PIL import Image
import numpy as np
import random


def read_image(filename):
    imarr = np.array([])
    try:
        im = Image.open(os.path.join(filename))
        im = im.convert("L")  
        imarr = np.array(im, dtype=np.uint8)
    except IOError as (errno, strerror):
        print "I/O error({0}): {1}".format(errno, strerror)
    except:
        print "Cannot open image."
    return imarr


def asRowMatrix(X):
    
    if len(X) == 0:
        return np.array([])
    total = 1
    for i in range(0, np.ndim(X[0])):
        total = total * X[0].shape[i]
    mat = np.empty([0, total], dtype=X[0].dtype)
    for row in X:
        mat = np.append(mat, row.reshape(1, -1), axis=0)  
    return np.asmatrix(mat)


def asColumnMatrix(X):
    
    if len(X) == 0:
        return np.array([])
    total = 1
    for i in range(0, np.ndim(X[0])):
        total = total * X[0].shape[i]
    mat = np.empty([total, 0], dtype=X[0].dtype)
    for col in X:
        mat = np.append(mat, col.reshape(-1, 1), axis=1)  
    return np.asmatrix(mat)


def minmax_normalize(X, low, high, minX=None, maxX=None, dtype=np.float):
    
    if minX is None:
        minX = np.min(X)
    if maxX is None:
        maxX = np.max(X)
    minX = float(minX)
    maxX = float(maxX)
    
    X = X - minX
    X = X / (maxX - minX)
    
    X = X * (high - low)
    X = X + low
    return np.asarray(X, dtype=dtype)


def shuffle(X, y):
    idx = np.argsort([random.random() for i in xrange(y.shape[0])])
    return X[:, idx], y[idx]


def shuffle_array(X, y):
    
    idx = np.argsort([random.random() for i in xrange(len(y))])
    X = [X[i] for i in idx]
    y = [y[i] for i in idx]
    return X, y


def to_col_vec(row_vec):
    
    return row_vec[:, np.newaxis]


def to_row_vec(col_vec):
    
    return col_vec.reshape(1, -1)