import numpy as np


class AbstractFeature(object):
    def compute(self, X, y):
        raise NotImplementedError("Every AbstractFeature must implement the compute method.")

    def extract(self, X):
        raise NotImplementedError("Every AbstractFeature must implement the extract method.")

    def save(self):
        raise NotImplementedError("Not implemented yet (TODO).")

    def load(self):
        raise NotImplementedError("Not implemented yet (TODO).")

    def __repr__(self):
        return self.short_name()

    def short_name(self):
        return self.__class__.__name__


class Identity(AbstractFeature):
    

    def __init__(self):
        AbstractFeature.__init__(self)

    def compute(self, X, y):
        return X

    def extract(self, X):
        return X

    def __repr__(self):
        return "Identity"


from facerec_py.facerec.util import asColumnMatrix
from facerec_py.facerec.operators import ChainOperator, CombineOperator


class PCA(AbstractFeature):
    def __init__(self, num_components=0):
        AbstractFeature.__init__(self)
        self._num_components = num_components
        self._total_energy = 0
        self._mean = None
        self._eigenvectors = None
        self._eigenvalues = None

    def compute(self, X, y):
        
        
        XC = asColumnMatrix(X)
        y = np.asarray(y)

        
        if self._num_components <= 0 or (self._num_components > XC.shape[1] - 1):
            self._num_components = XC.shape[1] - 1  

        
        self._mean = XC.mean(axis=1).reshape(-1, 1)
        XC = XC - self._mean

        
        self._eigenvectors, self._eigenvalues, variances = np.linalg.svd(XC, full_matrices=False)

        
        self._eigenvalues = np.power(self._eigenvalues, 2) / XC.shape[1]

        
        self._total_energy = np.sum(self._eigenvalues)

        idx = np.argsort(-self._eigenvalues)
        self._eigenvalues, self._eigenvectors = self._eigenvalues[idx], self._eigenvectors[:, idx]

        
        self._eigenvectors = self._eigenvectors[:, :self._num_components].copy()
        self._eigenvalues = self._eigenvalues[:self._num_components].copy()

        
        features = []
        for x in X:
            xp = self.project(x.reshape(-1, 1))
            features.append(xp)
        return features

    def extract(self, X):
        X = np.asarray(X).reshape(-1, 1)
        return self.project(X)

    def project(self, X):
        X = X - self._mean
        return np.dot(self._eigenvectors.T, X)

    def reconstruct(self, X):
        X = np.dot(self._eigenvectors, X)  
        return X + self._mean

    @property
    def num_components(self):
        return self._num_components

    @property
    def eigenvalues(self):
        return self._eigenvalues

    @property
    def eigenvectors(self):
        return self._eigenvectors

    @property
    def mean(self):
        return self._mean

    @property
    def energy_percentage(self):
        return np.sum(self._eigenvalues) / self._total_energy

    def __repr__(self):
        return "PCA (num_components=%d)" % self._num_components

    def short_name(self):
        return "PCA: %d" % self._num_components


class LDA(AbstractFeature):
    def __init__(self, num_components=0):
        AbstractFeature.__init__(self)
        self._num_components = num_components
        self._eigenvalues = None
        self._eigenvectors = None

    def compute(self, X, y):
        
        XC = asColumnMatrix(X)
        y = np.asarray(y)
        
        d = XC.shape[0]
        c = len(np.unique(y))
        
        if self._num_components <= 0:
            self._num_components = c - 1
        elif self._num_components > (c - 1):
            self._num_components = c - 1

        
        mean_total = XC.mean(axis=1).reshape(-1, 1)  

        
        Sw = np.zeros((d, d), dtype=np.float32)
        Sb = np.zeros((d, d), dtype=np.float32)
        for i in range(0, c):
            Xi = XC[:, np.where(y==i)[0]]
            mean_class = np.mean(Xi, axis=1).reshape(-1, 1)
            Sw = Sw + np.dot((Xi - mean_class), (Xi - mean_class).T)
            Sb = Sb + Xi.shape[1] * np.dot((mean_class - mean_total), (mean_class - mean_total).T)

        
        self._eigenvalues, self._eigenvectors = np.linalg.eig(np.linalg.inv(Sw) * Sb)

        
        idx = np.argsort(-self._eigenvalues.real)
        self._eigenvalues, self._eigenvectors = self._eigenvalues[idx], self._eigenvectors[:, idx]
        
        self._eigenvalues = np.array(self._eigenvalues[0:self._num_components].real, dtype=np.float32, copy=True)
        self._eigenvectors = np.matrix(self._eigenvectors[0:, 0:self._num_components].real, dtype=np.float32, copy=True)

        
        features = []
        for x in X:
            xp = self.project(x.reshape(-1, 1))
            features.append(xp)
        return features

    def project(self, X):
        return np.dot(self._eigenvectors.T, X)

    def reconstruct(self, X):
        return np.dot(self._eigenvectors, X)

    @property
    def num_components(self):
        return self._num_components

    @property
    def eigenvectors(self):
        return self._eigenvectors

    @property
    def eigenvalues(self):
        return self._eigenvalues

    def __repr__(self):
        return "LDA (num_components=%d)" % self._num_components


class Fisherfaces(AbstractFeature):
    def __init__(self, num_components=0):
        AbstractFeature.__init__(self)
        self._num_components = num_components
        self._eigenvectors = None
        self._eigenvalues = None

    def compute(self, X, y):
        
        XC = asColumnMatrix(X)
        y = np.asarray(y)
        
        n = len(y)
        c = len(np.unique(y))

        
        pca = PCA(num_components=(n-c))
        lda = LDA(num_components=self._num_components)
        
        model = ChainOperator(pca, lda)
        
        model.compute(X, y)

        
        self._eigenvalues = lda.eigenvalues
        self._num_components = lda.num_components
        
        self._eigenvectors = np.dot(pca.eigenvectors, lda.eigenvectors)

        
        features = []
        for x in X:
            xp = self.project(x.reshape(-1, 1))
            features.append(xp)
        return features

    def extract(self, X):
        X = np.asarray(X).reshape(-1, 1)
        return self.project(X)

    def project(self, X):
        return np.dot(self._eigenvectors.T, X)

    def reconstruct(self, X):
        return np.dot(self._eigenvectors, X)

    @property
    def num_components(self):
        return self._num_components

    @property
    def eigenvalues(self):
        return self._eigenvalues

    @property
    def eigenvectors(self):
        return self._eigenvectors

    def __repr__(self):
        return "Fisherfaces (num_components=%s)" % self._num_components

    def short_name(self):
        return "Fisher: %d" % self._num_components


from facerec_py.facerec.lbp import *


class SpatialHistogram(AbstractFeature):
    def __init__(self, lbp_operator=ExtendedLBP(), sz=(8, 8)):
        
        AbstractFeature.__init__(self)
        if not isinstance(lbp_operator, LocalDescriptor):
            raise TypeError("Only an operator of type facerec.lbp.LocalDescriptor is a valid lbp_operator.")
        self.lbp_operator = lbp_operator
        self.sz = sz
        self.X = None
        self.y = None

    def compute(self, X, y):
        self.X = X
        self.y = y

        features = []
        for x in X:
            x = np.asarray(x)  
            h = self.spatially_enhanced_histogram(x)
            features.append(h)
        return features

    def extract(self, X):
        X = np.asarray(X)
        return self.spatially_enhanced_histogram(X)

    def spatially_enhanced_histogram(self, X):
        
        
        L = self.lbp_operator(X)  

        
        lbp_height, lbp_width = L.shape
        grid_rows, grid_cols = self.sz
        
        py = int(np.floor(lbp_height/grid_rows))
        px = int(np.floor(lbp_width/grid_cols))

        E = []
        for row in range(0, grid_rows):
            for col in range(0, grid_cols):
                C = L[row*py:(row+1)*py, col*px:(col+1)*px]  
                H = self._get_histogram(C, row, col)
                
                E.extend(H)
        return np.asarray(E)

    def _get_histogram(self, C, row, col, normed=True):
        H = np.histogram(C,
                         bins=2 ** self.lbp_operator.neighbors,  
                         range=(0, 2 ** self.lbp_operator.neighbors),
                         weights=None,
                         normed=normed
        )[0]  
        return H

    def __repr__(self):
        return "SpatialHistogram LBP (operator=%s, grid=%s)" % (repr(self.lbp_operator), str(self.sz))

    def short_name(self):
        return "LBP Histogram