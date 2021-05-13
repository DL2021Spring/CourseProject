



































import numpy as np
from scipy import ndimage
import os
import sys

sys.path.append("../..")


try:
    from PIL import Image
except ImportError:
    import Image

import matplotlib.pyplot as plt
import textwrap

import logging

from facerec.feature import SpatialHistogram
from facerec.distance import ChiSquareDistance
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
from facerec.lbp import LPQ, ExtendedLBP
from facerec.validation import SimpleValidation, precision
from facerec.util import shuffle_array

EXPERIMENT_NAME = "LocalPhaseQuantizationExperiment"





ITER_MAX = 1

class FileNameFilter:
    
    def __init__(self, name):
        self._name = name

    def __call__(self, filename):
        return True
        
    def __repr__(self):
        return "FileNameFilter (name=%s)" % (self._name) 


class YaleBaseFilter(FileNameFilter):
    
    def __init__(self, min_azimuth, max_azimuth, min_elevation, max_elevation):
        FileNameFilter.__init__(self, "Filter YaleFDB Subset1")
        self._min_azimuth = min_azimuth
        self._max_azimuth = max_azimuth
        self._min_elevation = min_elevation
        self._max_elevation = max_elevation

    def __call__(self, filename):
        
        
        filetype = filename[-4:]
        if filetype != ".pgm":
            return False

        
        if "Ambient" in filename:
            return False
        
        azimuth = abs(int(filename[12:16]))
        elevation = abs(int(filename[17:20]))

        
        if azimuth < self._min_azimuth or azimuth > self._max_azimuth:
            return False
        if elevation < self._min_elevation or elevation > self._max_elevation:
            return False
            
        return True

    def __repr__(self):
        return "Yale FDB Filter (min_azimuth=%s, max_azimuth=%s, min_elevation=%s, max_elevation=%s)" % (min_azimuth, max_azimuth, min_elevation, max_elevation)


def read_images(path, fileNameFilter=FileNameFilter("None"), sz=None):
    
    c = 0
    X,y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                if fileNameFilter(filename):
                    try:
                        im = Image.open(os.path.join(subject_path, filename))
                        im = im.convert("L")
                        
                        if (sz is not None):
                            im = im.resize(sz, Image.ANTIALIAS)
                        X.append(np.asarray(im, dtype=np.uint8))
                        y.append(c)
                    except IOError, (errno, strerror):
                        print "I/O error({0}): {1}".format(errno, strerror)
                    except:
                        print "Unexpected error:", sys.exc_info()[0]
                        raise         
            c = c+1
    return [X,y]
    
def apply_gaussian(X, sigma):
    
    return np.array([ndimage.gaussian_filter(x, sigma) for x in X])


def results_to_list(validation_results):
    return [precision(result.true_positives,result.false_positives) for result in validation_results]
    
def partition_data(X, y):
    
    Xs,ys = shuffle_array(X,y)
    
    mapping = {}
    for i in xrange(len(y)):
        yi = ys[i]
        try:
            mapping[yi].append(i)
        except KeyError:
            mapping[yi] = [i]
    
    Xtrain, ytrain = [], []
    Xtest, ytest = [], []
    
    for key, indices in mapping.iteritems():
        
        Xtrain.extend([ Xs[i] for i in indices[:1] ])
        ytrain.extend([ ys[i] for i in indices[:1] ])
        Xtest.extend([ Xs[i] for i in indices[1:20]])
        ytest.extend([ ys[i] for i in indices[1:20]])
    
    return Xtrain, ytrain, Xtest, ytest

class ModelWrapper:
    def __init__(model):
        self.model = model
        self.result = []

if __name__ == "__main__":
    
    
    out_dir = None
    
    
    
    if len(sys.argv) < 2:

        print "USAGE: lpq_experiment.py </path/to/images>"
        sys.exit()
    
    yale_subset_0_40 = YaleBaseFilter(0, 40, 0, 40)
    
    [X,y] = read_images(sys.argv[1], yale_subset_0_40, sz=(64,64))
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger = logging.getLogger("facerec")
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    model0 = PredictableModel(feature=SpatialHistogram(lbp_operator=ExtendedLBP()), classifier=NearestNeighbor(dist_metric=ChiSquareDistance(), k=1))
    model1 = PredictableModel(feature=SpatialHistogram(lbp_operator=LPQ()), classifier=NearestNeighbor(dist_metric=ChiSquareDistance(), k=1))
    
    sigmas = [0]
    print 'The experiment will be run %s times!' % ITER_MAX
    
    experiments = {}
    experiments['lbp_model'] = { 'model': model0, 'results' : {}, 'color' : 'r', 'linestyle' : '--', 'marker' : '*'} 
    experiments['lpq_model'] = { 'model': model1, 'results' : {}, 'color' : 'b', 'linestyle' : '--', 'marker' : 's'}
    
    for sigma in sigmas:
        print "Setting sigma=%s" % sigma
        for key, value in experiments.iteritems():
            print 'Running experiment for model=%s' % key
            
            cv0 = SimpleValidation(value['model'])
            for iteration in xrange(ITER_MAX):
                print "Repeating experiment %s/%s." % (iteration + 1, ITER_MAX)
                
                Xtrain, ytrain, Xtest, ytest = partition_data(X,y)
                
                Xs = apply_gaussian(Xtest, sigma)
                
                experiment_description = "%s (iteration=%s, sigma=%.2f)" % (EXPERIMENT_NAME, iteration, sigma)
                cv0.validate(Xtrain, ytrain, Xs, ytest, experiment_description)
            
            true_positives = sum([validation_result.true_positives for validation_result in cv0.validation_results])
            false_positives = sum([validation_result.false_positives for validation_result in cv0.validation_results])
            
            prec = precision(true_positives,false_positives)
            
            print key
            experiments[key]['results'][sigma] = prec

    
    fig = plt.figure()
    
    plot_legend = []
    
    for experiment_name, experiment_definition in experiments.iteritems():
        print key, experiment_definition
        results = experiment_definition['results']
        (xvalues, yvalues) = zip(*[(k,v) for k,v in results.iteritems()])
        
        plot_legend.append(experiment_name)
        
        plot_color = experiment_definition['color']
        plot_linestyle = experiment_definition['linestyle']
        plot_marker = experiment_definition['marker']
        plt.plot(sigmas, yvalues, linestyle=plot_linestyle, marker=plot_marker, color=plot_color)
    
    plt.legend(plot_legend, prop={'size':6}, numpoints=1, loc='upper center', bbox_to_anchor=(0.5, -0.2),  fancybox=True, shadow=True, ncol=1)
    
    plt.ylim(0,1)
    plt.xlim(-0.2, max(sigmas) + 1)
    
    plt.title(EXPERIMENT_NAME)
    plt.ylabel('Precision')
    plt.xlabel('Sigma')
    fig.subplots_adjust(bottom=0.5)
    
    plt.savefig("lpq_experiment.png", bbox_inches='tight',dpi=100)
