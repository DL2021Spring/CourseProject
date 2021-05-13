from facerec_py.facerec.distance import EuclideanDistance
from facerec_py.facerec.normalization import gaussian_kernel, inverse_dissim
from facerec_py.facerec.util import asRowMatrix
import logging
import numpy as np
import operator as op


class AbstractClassifier(object):
    def compute(self, X, y):
        raise NotImplementedError("Every AbstractClassifier must implement the compute method.")

    def predict(self, X):
        raise NotImplementedError("Every AbstractClassifier must implement the predict method.")

    def update(self, X, y):
        raise NotImplementedError("This Classifier is cannot be updated.")

    def binary_predict(self, q, lbl):
        
        raise NotImplementedError("The binary prediction is not implemented")


class NearestNeighbor(AbstractClassifier):
    

    def __init__(self, dist_metric=EuclideanDistance(), k=1):
        AbstractClassifier.__init__(self)
        self.k = k
        self.dist_metric = dist_metric
        self.X = []
        self.y = np.array([], dtype=np.int32)

    def update(self, X, y):
        
        self.X.append(X)
        self.y = np.append(self.y, y)

    def compute(self, X, y):
        self.X = X  
        self.y = np.asarray(y)

    def predict(self, q):
        
        distances = []
        for xi in self.X:
            xi = xi.reshape(-1, 1)
            d = self.dist_metric(xi, q)
            distances.append(d)
        if len(distances) > len(self.y):
            raise Exception("More distances than classes. Is your distance metric correct?")
        distances = np.asarray(distances)
        
        idx = np.argsort(distances)
        
        sorted_y = self.y[idx]
        sorted_distances = distances[idx]
        sorted_sim = inverse_dissim(sorted_distances)
        
        
        
        

        
        hist = dict((key, val) for key, val in enumerate(np.bincount(sorted_y[:self.k])) if val)
        predicted_label = max(hist.iteritems(), key=op.itemgetter(1))[0]

        
        
        
        
        
        return [predicted_label, {'labels': sorted_y, 'distances': sorted_distances, 'similarities': sorted_sim}]

    def __repr__(self):
        return "NearestNeighbor (k=%s, dist_metric=%s)" % (self.k, repr(self.dist_metric))


try:
    from svmutil import *
except ImportError:
    logger = logging.getLogger("facerec.classifier.SVM")
    logger.debug("Import Error: libsvm bindings not available.")
except:
    logger = logging.getLogger("facerec.classifier.SVM")
    logger.debug("Import Error: libsvm bindings not available.")

import sys
from StringIO import StringIO
from svmutil import *

bkp_stdout = sys.stdout


class SVM(AbstractClassifier):
    

    def __init__(self, param=None):
        AbstractClassifier.__init__(self)
        self.logger = logging.getLogger("facerec.classifier.SVM")
        self.param = param
        self.svm = svm_model()
        self.param = param
        if self.param is None:
            self.param = svm_parameter("-q")

    def compute(self, X, y):
        self.logger.debug("SVM TRAINING (C=%.2f,gamma=%.2f,p=%.2f,nu=%.2f,coef=%.2f,degree=%.2f)" % (
            self.param.C, self.param.gamma, self.param.p, self.param.nu, self.param.coef0, self.param.degree))
        
        X = asRowMatrix(X)
        y = np.asarray(y)
        problem = svm_problem(y, X.tolist())
        self.svm = svm_train(problem, self.param)
        self.y = y

    def predict(self, X):
        
        X = np.asarray(X).reshape(1, -1)
        sys.stdout = StringIO()
        p_lbl, p_acc, p_val = svm_predict([0], X.tolist(), self.svm)
        sys.stdout = bkp_stdout
        predicted_label = int(p_lbl[0])
        return [predicted_label, {'p_lbl': p_lbl, 'p_acc': p_acc, 'p_val': p_val}]

    def __repr__(self):
        return "Support Vector Machine (kernel_type=%s, C=%.2f,gamma=%.2f,p=%.2f,nu=%.2f,coef=%.2f,degree=%.2f)" % (
            self.param.kernel_type, self.param.C, self.param.gamma, self.param.p, self.param.nu,
            self.param.coef0, self.param.degree)


