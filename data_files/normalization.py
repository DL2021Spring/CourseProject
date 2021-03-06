
import numpy as np


def minmax(X, low, high, minX=None, maxX=None, dtype=np.float):
    X = np.asarray(X)
    if minX is None:
        minX = np.min(X)
    if maxX is None:
        maxX = np.max(X)
    
    X -= float(minX)
    X /= float((maxX - minX))
    
    X = X * (high - low)
    X = X + low
    return np.asarray(X, dtype=dtype)


def zscore(X, mean=None, std=None):
    
    X = np.asarray(X)
    if mean is None:
        mean = X.mean()
    if std is None:
        std = X.std()
    X = (X - mean) / std
    return X


def gaussian(X, mu, sig):
    return (1/(sig*np.sqrt(2*np.pi)))*\
           np.exp(-(X-mu)**2/(2*sig**2))


def inverse_dissim(X):
    
    X = np.asarray(X)
    X = zscore(X)
    X = minmax(X, 0, 10)
    return 1./(1+X)


def vector_normalize(x):
    return x / np.linalg.norm(x)


def gaussian_kernel(X, mu=None, sig=None):
    
    X = np.asarray(X)
    if mu is None:
        mu = X.mean()
    if sig is None:
        sig = X.std()

    return np.exp(-np.power(X-mu, 2)/(2*sig**2))