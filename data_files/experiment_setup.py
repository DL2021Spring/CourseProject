import sys
from expr.weighted_hs import WeightedLGBPHS

from facerec_py.facerec.distance import *
from facerec_py.facerec.classifier import NearestNeighbor, SVM
from facerec_py.facerec.model import PredictableModel, FeaturesEnsemblePredictableModel
from facerec_py.facerec.validation import KFoldCrossValidation, shuffle
from facerec_py.facerec.visual import subplot
from facerec_py.facerec.util import minmax_normalize
from expr.read_dataset import read_images
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from expr.feature import *
from util.commons_util.logger_utils.logger_factory import LoggerFactory
from scipy.interpolate import spline
import numpy as np

__author__ = 'Danyang'


class Drawer(object):
    def __init__(self, smooth=False):
        plt.figure("ROC")
        plt.axis([0, 0.5, 0.5, 1.001])
        
        
        plt.xlabel('FPR')
        plt.ylabel('TPR')
        
        plt.rc('axes', color_cycle=['r', 'g', 'b', 'c', 'm', 'y', 'k',
                                    'darkgreen', 'chocolate', 'darksalmon', 'darkseagreen', 'yellowgreen'])
        self.is_smooth = smooth
        self._rocs = []

    def show(self):
        plt.legend(handles=self._rocs)
        plt.show()

    def plot_roc(self, cv):
        
        
        FPRs = [r.FPR for r in cv.validation_results]
        TPRs = [r.TPR for r in cv.validation_results]

        
        FPRs.append(0.0)
        TPRs.append(0.0)
        FPRs.append(1.0)
        TPRs.append(1.0)

        if self.is_smooth:
            FPRs, TPRs = self.smooth(FPRs, TPRs)

        
        roc, = plt.plot(FPRs, TPRs, label=cv.model.feature.short_name())
        self._rocs.append(roc)

    def smooth(self, x, y):
        x = np.array(x)
        y = np.array(y)
        x, idx = np.unique(x, return_index=True)  
        y = y[idx]

        x_sm = np.linspace(x.min(), x.max(), 60)  
        y_sm = spline(x, y, x_sm)
        return x_sm, y_sm


class Experiment(object):
    def __init__(self, smooth=False, froze_shuffle=False):
        
        self.logger = LoggerFactory().getConsoleLogger("facerec")
        self._drawer = Drawer(smooth)
        self.X, self.y = shuffle(*self.read())  
        self.froze_shuffle = froze_shuffle  

    def read(self):
        
        
        out_dir = None
        
        
        
        if len(sys.argv) < 2:
            print "USAGE: experiment_setup.py </path/to/images>"
            sys.exit()
        
        X, y = read_images(sys.argv[1])

        X = np.asarray(X)
        y = np.asarray(y)
        return X, y

    def plot_fisher_original(self, X, model):
        E = []
        for i in xrange(min(model.feature.eigenvectors.shape[1], 16)):
            e = model.feature.eigenvectors[:, i].reshape(X[0].shape)
            E.append(minmax_normalize(e, 0, 255, dtype=np.uint8))
        
        subplot(title="Fisherfaces", images=E, rows=4, cols=4, sptitle="Fisherface", colormap=cm.jet,
                filename="fisherfaces.png")
        
        plt.close()

    def plot_fisher(self, X, model, r=3, c=5):
        
        E = []
        for i in xrange(min(model.feature.eigenvectors.shape[1], r*c)):
            e = model.feature.eigenvectors[:, i].reshape(X[0].shape)
            E.append(minmax_normalize(e, 0, 255, dtype=np.uint8))

        
        subplot(title="Fisherface Components", images=E, rows=r, cols=c, sptitle="fisherface", colormap=cm.rainbow,
                filename="fisherfaces.png")
        plt.close()


    def experiment(self, feature=Fisherfaces(), plot=None, dist_metric=EuclideanDistance(), threshold_up=0, kNN_k=1, number_folds=None, debug=True):
        
        
        classifier = NearestNeighbor(dist_metric=dist_metric, k=kNN_k)
        
        
        model = self._get_model(feature, classifier)
        
        model.compute(self.X, self.y)
        
        
        if plot:
            plot(self.X, model)
        
        
        if number_folds is None:
            number_folds = len(np.unique(self.y))
            if number_folds>15: number_folds = 10


        cv = KFoldCrossValidation(model, k=number_folds, threshold_up=threshold_up, froze_shuffle=self.froze_shuffle, debug=debug)
        
        cv.validate(self.X, self.y)

        
        print cv
        if debug:
            self.logger.info("Cross validation completed; press any key on any image to continue")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return cv

    def _get_model(self, feature, classifier):
        return PredictableModel(feature=feature, classifier=classifier)

    def show_plot(self):
        
        self._drawer.show()

    def plot_roc(self, cv):
        
        self._drawer.plot_roc(cv)


class FeaturesEnsembleExperiment(Experiment):
    def _get_model(self, features, classifier):
        return FeaturesEnsemblePredictableModel(features, classifier)


def draw_roc(expr):
    
    cv = expr.experiment(Fisherfaces(14), threshold_up=1)
    expr.plot_roc(cv)
    cv = expr.experiment(PCA(50), threshold_up=1)
    expr.plot_roc(cv)
    cv = expr.experiment(SpatialHistogram(), dist_metric=HistogramIntersection(), threshold_up=1)
    expr.plot_roc(cv)

    expr.show_plot()


def ensemble_lbp_fisher():
    
    features = [LbpFisher(ExtendedLBP(i)) for i in (3, 6, 10, 11, 14, 15, 19)]
    expr = FeaturesEnsembleExperiment()
    expr.experiment(features, debug=False)


if __name__ == "__main__":
    expr = Experiment(froze_shuffle=True)
    
    
    
    
    
    
    
    
    
    