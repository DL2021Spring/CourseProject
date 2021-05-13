from __future__ import absolute_import
import math as math
import random as random
import logging
import cv2

import numpy as np

from facerec_py.facerec.model import PredictableModel, AbstractPredictableModel
from util.commons_util.fundamentals.generators import frange















class TFPN(object):
    def __init__(self, TP=0, FP=0, TN=0, FN=0):
        self.rates = np.array([TP, FP, TN, FN], dtype=np.double)

    @property
    def TP(self):
        return self.rates[0]

    @TP.setter
    def TP(self, value):
        self.rates[0] = value

    @property
    def FP(self):
        return self.rates[1]

    @FP.setter
    def FP(self, value):
        self.rates[1] = value

    @property
    def TN(self):
        return self.rates[2]

    @TN.setter
    def TN(self, value):
        self.rates[2] = value

    @property
    def FN(self):
        return self.rates[3]

    @FN.setter
    def FN(self, value):
        self.rates[3] = value

    def __add__(self, other):
        return self.rates + other.rates

    def __iadd__(self, other):
        self.rates += other.rates
        return self


def shuffle(X, y):
    
    idx = np.argsort([random.random() for _ in xrange(len(y))])  
    X = [X[i] for i in idx]
    y = y[idx]
    return X, y


def slice_2d(X, rows, cols):
    
    return [X[i][j] for j in cols for i in rows]


def precision(true_positives, false_positives):
    
    return accuracy(true_positives, 0, false_positives, 0)


def accuracy(true_positives, true_negatives, false_positives, false_negatives, description=None):
    
    true_positives = float(true_positives)
    true_negatives = float(true_negatives)
    false_positives = float(false_positives)
    false_negatives = float(false_negatives)
    if (true_positives + true_negatives + false_positives + false_negatives) < 1e-15:
        return 0.0
    return (true_positives + true_negatives) / (true_positives + false_positives + true_negatives + false_negatives)


class ValidationResult(object):
    

    def __init__(self, true_positives, true_negatives, false_positives, false_negatives, description):
        self.true_positives = true_positives
        self.true_negatives = true_negatives
        self.false_positives = false_positives
        self.false_negatives = false_negatives
        self.description = description

    def __div(self, x, y):
        
        if y < 1e-15:
            return 0.0
        return x/y

    @property
    def TPR(self):
        return self.__div(self.true_positives, self.true_positives+self.false_negatives)

    @property
    def FPR(self):
        return self.__div(self.false_positives, self.false_positives+self.true_negatives)

    @property
    def recall(self):
        return self.__div(self.true_positives, self.true_positives+self.false_negatives)

    @property
    def precision(self):
        return self.__div(self.true_positives, self.true_positives+self.false_positives)

    @property
    def total(self):
        return self.true_negatives+self.true_positives+self.false_negatives+self.false_positives
    @property
    def accuracy(self):
        return self.__div(self.true_positives+self.true_negatives, self.total)

    @property
    def F1(self):
        return self.__div(2*self.precision*self.recall, self.precision+self.recall)

    def __repr__(self):
        return "ValidationResult (Description=%s, Precision=%.2f%%, Recall=%.2f%%, TPR=%.2f%%, FPR=%.2f%%, TP=%d, TN=%d, FP=%d, FN=%d)" % (
            self.description, self.precision*100, self.recall*100, self.TPR*100, self.FPR*100, self.true_positives, self.true_negatives, self.false_positives, self.false_negatives)


class ValidationStrategy(object):
    

    def __init__(self, model):
        
        if not isinstance(model, AbstractPredictableModel):
            raise TypeError("Validation can only validate the type PredictableModel.")
        self.model = model
        self.validation_results = []

    def add(self, validation_result):
        self.validation_results.append(validation_result)

    def validate(self, X, y, description):
        
        raise NotImplementedError("Every Validation module must implement the validate method!")

    def print_results(self):
        print self.model
        for validation_result in self.validation_results:
            print validation_result

    def __repr__(self):
        return "Validation Strategy (model=%s, results=%s)"%(self.model, self.validation_results)


class KFoldCrossValidation(ValidationStrategy):
    

    def __init__(self, model, k=10, threshold_up=1, froze_shuffle=False, debug=True):
        
        super(KFoldCrossValidation, self).__init__(model=model)
        self.threshold_up = threshold_up
        self.k = k
        self.logger = logging.getLogger("facerec.validation.KFoldCrossValidation")
        self._debug = debug
        self.froze_shuffle = froze_shuffle

    def validate(self, X, y, description="ExperimentName"):
        
        if not self.froze_shuffle:
            X, y = shuffle(X, y)

        c = len(np.unique(y))
        foldIndices = []
        n = np.iinfo(np.int).max  
        for i in range(0, c):
            idx = np.where(y == i)[0]  
            n = min(n, idx.shape[0])
            foldIndices.append(idx.tolist());

        
        
        
        
        if n < self.k:
            self.k = n

        
        foldSize = int(math.floor(n / self.k))

        if self.threshold_up==0:
            threshold_r = [0]
        else:
            threshold_r = frange(0, self.threshold_up, 0.001)

        rates = {}
        for threshold in threshold_r:
            rates[threshold] = TFPN()

        for i in range(0, self.k):
            self.logger.info("Processing fold %d/%d." % (i + 1, self.k))

            
            l = int(i * foldSize)
            h = int((i + 1) * foldSize)
            
            
            testIdx = slice_2d(foldIndices, rows=range(0, c), cols=range(l, h))
            trainIdx = slice_2d(foldIndices, rows=range(0, c), cols=range(0, l))
            trainIdx.extend(slice_2d(foldIndices, rows=range(0, c), cols=range(h, n)))

            
            Xtrain = [X[t] for t in trainIdx]
            ytrain = y[trainIdx]

            self.model.compute(Xtrain, ytrain)

            predictions = {}
            for j in testIdx:
                predictions[j] = self.model.predict(X[j])

            if self.threshold_up == 0:  
                rates[threshold] += self.simple_evaluate(testIdx, predictions, X, y)
            else:  
                for threshold in threshold_r:
                    rates[threshold] += self.binary_evaluate(testIdx, predictions, X, y, threshold)

        for threshold in threshold_r:
            r = rates[threshold]
            self.add(ValidationResult(r.TP, r.TN, r.FP, r.FN, threshold))

    def simple_evaluate(self, testIdX, predictions, X, y):
        r = TFPN()
        for j in testIdX:
            prediction, info = predictions[j]
            if prediction==y[j]:
                r.TP += 1
            else:
                r.FP += 1
                if self._debug:
                    self.display_prediction_error(X[j], y[j], prediction)
        return r

    def display_prediction_error(self, data, actual, predicted):
        
        error_msg = "%d!=%d" % (actual, predicted)
        self.logger.debug("prediction error, actual!=predicted: " + error_msg)
        cv2.imshow(error_msg, data)
        cv2.waitKey(1)

    def binary_evaluate(self, testIdX, predictions, X, y, threshold):
        
        r = TFPN()
        for lbl in np.unique(y):
            for j in testIdX:
                _, info = predictions[j]
                labels = info['labels']
                idx = labels==lbl

                sims = info['similarities']
                sims = sims[idx]
                sims = sims[:1]  
                score = np.sum(sims)/float(sims.size)
                if score>threshold:  
                    if lbl==y[j]:
                        r.TP += 1
                    else:
                        r.FP += 1
                else:  
                    if lbl==y[j]:
                        r.FN += 1
                    else:
                        r.TN += 1
        
        return r

    def __repr__(self):
        return "k-Fold Cross Validation (model=%s, k=%s, results=%s)" % (self.model, self.k, self.validation_results)


class LeaveOneOutCrossValidation(ValidationStrategy):
    

    def __init__(self, model, k=0):
        
        super(LeaveOneOutCrossValidation, self).__init__(model=model)
        self.logger = logging.getLogger("facerec.validation.LeaveOneOutCrossValidation")
        self.k = k

    def validate(self, X, y, description="ExperimentName"):
        
        X, y = shuffle(X, y)
        true_positives, false_positives, true_negatives, false_negatives = (0, 0, 0, 0)
        if self.k==0:
            self.k = y.shape[0]

        for i in range(0, self.k):
            self.logger.info("Processing fold %d/%d." % (i + 1, self.k))

            
            trainIdx = []
            trainIdx.extend(range(0, i))
            trainIdx.extend(range(i + 1, self.k))

            
            Xtrain = [X[t] for t in trainIdx]
            ytrain = y[trainIdx]

            
            self.model.compute(Xtrain, ytrain)

            
            prediction = self.model.predict(X[i])[0]
            if prediction == y[i]:
                true_positives += 1
            else:
                false_positives += 1

        self.add(ValidationResult(true_positives, true_negatives, false_positives, false_negatives, description))

    def __repr__(self):
        return "Leave-One-Out Cross Validation (model=%s, results=%s)"%(self.model, self.validation_results)


class LeaveOneClassOutCrossValidation(ValidationStrategy):
    

    def __init__(self, model):
        
        super(LeaveOneClassOutCrossValidation, self).__init__(model=model)
        self.logger = logging.getLogger("facerec.validation.LeaveOneClassOutCrossValidation")

    def validate(self, X, y, g, description="ExperimentName"):
        
        true_positives, false_positives, true_negatives, false_negatives = (0, 0, 0, 0)

        for i in range(0, len(np.unique(y))):
            self.logger.info("Validating Class %s." % i)
            
            trainIdx = np.where(y != i)[0]
            testIdx = np.where(y == i)[0]
            
            Xtrain = [X[t] for t in trainIdx]
            gtrain = g[trainIdx]

            
            self.model.compute(Xtrain, gtrain)

            for j in testIdx:
                
                prediction = self.model.predict(X[j])[0]
                if prediction == g[j]:
                    true_positives += 1
                else:
                    false_positives += 1
        self.add(ValidationResult(true_positives, true_negatives, false_positives, false_negatives, description))

    def __repr__(self):
        return "Leave-One-Class-Out Cross Validation (model=%s, results=%s)"%(self.model, self.validation_results)


class SimpleValidation(ValidationStrategy):
    

    def __init__(self, model):
        
        super(SimpleValidation, self).__init__(model=model)
        self.logger = logging.getLogger("facerec.validation.SimpleValidation")

    def validate(self, Xtrain, ytrain, Xtest, ytest, description="ExperimentName"):
        
        self.logger.info("Simple Validation.")

        self.model.compute(Xtrain, ytrain)

        self.logger.debug("Model computed.")

        true_positives, false_positives, true_negatives, false_negatives = (0, 0, 0, 0)
        count = 0
        for i in ytest:
            self.logger.debug("Predicting %s/%s." % (count, len(ytest)))
            prediction = self.model.predict(Xtest[i])[0]
            if prediction == ytest[i]:
                true_positives += 1
            else:
                false_positives += 1
            count += 1
        self.add(ValidationResult(true_positives, true_negatives, false_positives, false_negatives, description))

    def __repr__(self):
        return "Simple Validation (model=%s)" % self.model
