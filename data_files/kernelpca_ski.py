from facerec_py.facerec.feature import AbstractFeature
import numpy as np
from facerec_py.facerec.util import asColumnMatrix
from sklearn.decomposition import KernelPCA

__author__ = 'Danyang'


class KPCA(AbstractFeature):
    def __init__(self, num_components=50, kernel="poly", degree=3, coef0=0.0, gamma=None):
        AbstractFeature.__init__(self)
        self._num_components = num_components
        self._kernel = kernel
        self._degree = degree
        self._coef0 = coef0
        self._gamma = gamma

        self._kpca = None

    def compute(self, X, y):
        
        
        XC = asColumnMatrix(X)
        y = np.asarray(y)

        
        if self._num_components <= 0 or (self._num_components > XC.shape[1]-1):
            self._num_components = XC.shape[1]-1  

        
        self._mean = XC.mean(axis=1).reshape(-1,1)
        XC = XC - self._mean
        n_features = XC.shape[0]
        
        
        self._kpca = KernelPCA(n_components=self._num_components,
                               kernel=self._kernel,
                               degree=self._degree,
                               coef0=self._coef0,
                               gamma=self._gamma)

        self._kpca.fit(XC.T)

        features = []
        for x in X:
            features.append(self.extract(x))
        return features

    def extract(self,X):
        X = np.asarray(X).reshape(-1,1)
        return self.project(X)

    def project(self, X):
        
        X = X - self._mean
        return self._kpca.transform(X.T)

    @property
    def num_components(self):
        return self._num_components

    def __repr__(self):
        return "KernelPCA (num_components=%d)" % self._num_components

    def short_name(self):
        return "KernelPCA