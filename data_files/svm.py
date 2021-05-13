from facerec_py.facerec.classifier import SVM
from facerec_py.facerec.validation import KFoldCrossValidation
from facerec_py.facerec.model import PredictableModel
from svmutil import *
from itertools import product
import numpy as np
import logging


def range_f(begin, end, step):
    seq = []
    while True:
        if step == 0: break
        if step > 0 and begin > end: break
        if step < 0 and begin < end: break
        seq.append(begin)
        begin = begin + step
    return seq


def grid(grid_parameters):
    grid = []
    for parameter in grid_parameters:
        begin, end, step = parameter
        grid.append(range_f(begin, end, step))
    return product(*grid)


def grid_search(model, X, y, C_range=(-5,  15, 2), gamma_range=(3, -15, -2), k=5, num_cores=1):
    
    if not isinstance(model, PredictableModel):
        raise TypeError("GridSearch expects a PredictableModel. If you want to perform optimization on raw data use facerec.feature.Identity to pass unpreprocessed data!")
    if not isinstance(model.classifier, SVM):
        raise TypeError("GridSearch expects a SVM as classifier. Please use a facerec.classifier.SVM!")
    
    logger = logging.getLogger("facerec.svm.gridsearch")
    logger.info("Performing a Grid Search.")
    
    
    best_parameter = svm_parameter("-q")
    best_parameter.kernel_type = model.classifier.param.kernel_type
    best_parameter.nu = model.classifier.param.nu
    best_parameter.coef0 = model.classifier.param.coef0
    
    if (gamma_range is None) or (model.classifier.param.kernel_type == LINEAR):
        gamma_range = (0, 0, 1)
    
    
    best_accuracy = np.finfo('float').min
    
    
    g = grid([C_range, gamma_range])
    results = []
    for p in g:
        C, gamma = p
        C, gamma = 2**C, 2**gamma
        model.classifier.param.C, model.classifier.param.gamma = C, gamma

        
        cv = KFoldCrossValidation(model=model,k=k)
        cv.validate(X,y)

        
        results.append([C, gamma, cv.accuracy])
        
        
        if cv.accuracy > best_accuracy:
            logger.info("best_accuracy=%s" % (cv.accuracy))
            best_accuracy = cv.accuracy
            best_parameter.C, best_parameter.gamma = C, gamma
        
        logger.info("%d-CV Result = %.2f." % (k, cv.accuracy))
        
    
    return best_parameter, results
