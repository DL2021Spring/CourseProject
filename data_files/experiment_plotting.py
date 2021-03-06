from experiment_setup import *
import numpy as np
from expr.kernelpca_ski import KPCA
from util.commons_util.decorators.general import print_func_name

__author__ = 'Danyang'


class Plotter(object):
    def __init__(self):
        pass

    def _plot(self, models, dist_metric=EuclideanDistance()):
        expr = Experiment(froze_shuffle=True)
        for model in models:
            cv = expr.experiment(model, threshold_up=1, debug=False, dist_metric=dist_metric)
            expr.plot_roc(cv)
        expr.show_plot()

    def _simple_run(self, models, dist_metric=EuclideanDistance()):
        expr = Experiment(froze_shuffle=True)
        for model in models:
            expr.experiment(model, threshold_up=0, debug=False, dist_metric=dist_metric)


class PlotterPCA(Plotter):
    def plot_components(self):
        models = []
        for num_component in xrange(10, 150, 30):
            models.append(PCA(num_component))

        self._plot(models)

    def plot_energy(self):
        models = []

        class PCA_energy(PCA):
            def short_name(self):
                return "PCA: %.2f%%" % (self.energy_percentage * 100)

        for num_component in xrange(20, 110, 40):
            models.append(PCA_energy(num_component))

        self._plot(models)


class PlotterFisher(Plotter):
    def plot_components(self):
        models = []
        for num_components in xrange(1, 16, 3):
            models.append(Fisherfaces(num_components))

        self._plot(models)


class PlotterKnn(object):
    def plot_kNN(self):
        
        pca = PCA(40)
        expr = Experiment()

        plt.figure("PCA precision for different k in kNN")
        plt.xlabel("k of kNN")
        plt.ylabel("precision")

        xys = []
        for k in xrange(1, 41):
            cv = expr.experiment(pca, threshold_up=0, kNN_k=k, debug=False)
            xys.append((k, cv.validation_results[0].precision))

        plt.plot([elt[0] for elt in xys], [elt[1] for elt in xys])
        plt.show()


class PlotterLgbphs(Plotter):
    def _plot(self, models):
        super(PlotterLgbphs, self)._plot(models, HistogramIntersection())

    @print_func_name
    def plot_lbp_algorihtms(self):
        class LgbphsSub(LGBPHS2):
            def short_name(self):
                return "%s" % self.feature.model2.lbp_operator.short_name()

        models = []
        for lbp in (OriginalLBP(), ExtendedLBP(radius=6)):  
            models.append(LgbphsSub(lbp_operator=lbp))

        self._plot(models)

    @print_func_name
    def plot_gabor(self):
        class LgbphsSub(LGBPHS2):
            def short_name(self):
                return "LGBPHS"

        models = [LgbphsSub(lbp_operator=ExtendedLBP(3)),
                  SpatialHistogram(lbp_operator=ExtendedLBP(3))
        ]
        self._plot(models)


    @print_func_name
    def plot_scales(self, r=xrange(1, 10, 4)):  
        class LgbphsSub(LGBPHS2):
            def short_name(self):
                return "scale: %s" % self.feature.model1.scale_cnt

        self._plot([LgbphsSub(n_scale=i, lbp_operator=ExtendedLBP(3)) for i in r])

    @print_func_name
    def get_precision_scales(self, r=xrange(1, 10, 4)):
        self._simple_run([LGBPHS2(n_scale=i, lbp_operator=ExtendedLBP(3)) for i in r])

    @print_func_name
    def plot_orientations(self, r=xrange(2, 9, 3)):  
        class LgbphsSub(LGBPHS2):
            def short_name(self):
                return "orient: %s" % self.feature.model1.orient_cnt

        self._plot([LgbphsSub(n_orient=i, lbp_operator=ExtendedLBP(3)) for i in r])

    @print_func_name
    def get_precisions_orientations(self, r=xrange(2, 9, 3)):
        self._simple_run([LGBPHS2(n_orient=i, lbp_operator=ExtendedLBP(3)) for i in r])

    def plot_histogram(self):
        pass


class PlotterKernelPCA(Plotter):
    def plot_rbf(self, r=(10000.0 / (200 * 200), 0.5, 0.75, 1.0)):
        class KPCASub(KPCA):
            def short_name(self):
                return "%s, gamma=%.4f" % (self._kernel, self._gamma)

        self._plot([KPCASub(kernel="rbf", gamma=i) for i in r])

    def plot_poly_degree(self):
        
        models = []

        class KPCA_poly(KPCA):
            def short_name(self):
                return "poly (degree: %d)" % self._degree

        for degree in xrange(1, 6):
            models.append(KPCA_poly(50, "poly", degree))
        self._plot(models)

    def plot_poly_degree_precisions(self):
        
        expr = Experiment(froze_shuffle=True)

        plt.figure("Kernel PCA precision for different number of degrees")
        plt.xlabel("number of degrees")
        plt.ylabel("precision")

        class KPCA_poly(KPCA):
            def short_name(self):
                return "poly (degree: %d)" % self._degree

        xys = []
        for degree in (1, 4):
            cv = expr.experiment(KPCA_poly(10, "poly", degree), threshold_up=0, debug=False)
            xys.append((degree, cv.validation_results[0].precision))

        plt.plot([elt[0] for elt in xys], [elt[1] for elt in xys])
        plt.show()


    def plot_kernels(self):
        
        kernels = ["poly", "sigmoid", "cosine", "rbf"]
        models = []
        for kernel in kernels:
            models.append(KPCA(50, kernel))
        self._plot(models)

    def plot_poly_coef0(self, r=(0.0, 20.0, 40.0, 60.0, 80.0)):
        

        class KPCA_coef0(KPCA):
            def short_name(self):
                return "poly (coef0: %.2f)" % self._coef0

        self._plot([KPCA_coef0(kernel="poly", coef0=i) for i in r])

    def plot_poly_gamma(self, r=(10.0, 40.0, 70.0, 100.0, 130.0)):
        

        class KPCA_gamma(KPCA):
            def short_name(self):
                return "poly (gamma: %.2f)" % self._gamma

        self._plot([KPCA_gamma(kernel="poly", gamma=i) for i in r])

    def plot_sigmoid(self, r=(10.0, 20.0, 30.0, 40.0, 50.0)):
        

        class KPCA_sigmoid(KPCA):
            def short_name(self):
                return "sigmoid (gamma: %.2f)" % self._gamma

        self._plot([KPCA_sigmoid(kernel="sigmoid", gamma=i) for i in r])


class PlotterEnsemble(Plotter):
    def plot_fisher(self):
        expr = FeaturesEnsembleExperiment(froze_shuffle=True)
        plt.axis([0, 0.5, 0.9, 1.001])

        class LbpFisherSub(LbpFisher):
            def short_name(self):
                return "EnsembleLbpFisher"

        features = [LbpFisherSub(ExtendedLBP(i)) for i in (3, 6, 10, 11, 14, 15, 19)]  
        cv = expr.experiment(features, threshold_up=1, debug=False)
        expr.plot_roc(cv)

        features = [LbpFisher(ExtendedLBP(11))]
        cv = expr.experiment(features, threshold_up=1, debug=False)
        expr.plot_roc(cv)

        class FisherfacesSub(Fisherfaces):
            def short_name(self):
                return "Fisher"

        features = [FisherfacesSub(14)]
        cv = expr.experiment(features, threshold_up=1, debug=False)
        expr.plot_roc(cv)

        expr.show_plot()


class IdentityFold(Identity):
    def __init__(self, k):
        self.k = k
        super(IdentityFold, self).__init__()

    def short_name(self):
        return "folds - %d" % self.k


class PCAFold(PCA):
    def __init__(self, k, num_components):
        self.k = k
        super(PCAFold, self).__init__(num_components)

    def short_name(self):
        return "folds - %d" % self.k


class FisherFold(Fisherfaces):
    def __init__(self, k, num_components):
        self.k = k
        super(FisherFold, self).__init__(num_components)

    def short_name(self):
        return "folds - %d" % self.k


class Plotter1NN(Plotter):
    def plot_1NN(self):
        expr = Experiment()

        for number_folds in xrange(2, 12, 1):
            cv = expr.experiment(IdentityFold(number_folds), threshold_up=1, number_folds=number_folds, debug=False)
            expr.plot_roc(cv)

        expr.show_plot()

    def plot_1NN_PCA(self):
        expr = Experiment()

        class PCASub(PCA):
            def __init__(self, k, num_components):
                self.k = k
                super(PCASub, self).__init__(num_components)

            def short_name(self):
                return "folds - %d" % self.k

        for number_folds in xrange(2, 12, 1):
            cv = expr.experiment(PCASub(number_folds, 50), threshold_up=1, number_folds=number_folds, debug=False)
            expr.plot_roc(cv)

        expr.show_plot()

    def plot_1NN_Identity_Precisions(self):
        
        expr = Experiment(froze_shuffle=True)

        plt.figure("No reduction, precision for different number of folds")
        plt.xlabel("number of folds")
        plt.ylabel("precision")

        xys = []
        for number_folds in xrange(2, 12, 1):
            cv = expr.experiment(IdentityFold(number_folds), threshold_up=0, number_folds=number_folds, debug=False)
            xys.append((number_folds, cv.validation_results[0].precision))

        plt.plot([elt[0] for elt in xys], [elt[1] for elt in xys])
        plt.show()

    def plot_1NN_PCA_Precisions(self):
        
        expr = Experiment(froze_shuffle=True)

        plt.figure("PCA precision for different number of folds")
        plt.xlabel("number of folds")
        plt.ylabel("precision")

        xys = []
        for number_folds in xrange(2, 12, 1):
            cv = expr.experiment(PCAFold(number_folds, 40), threshold_up=0, number_folds=number_folds, debug=False)
            xys.append((number_folds, cv.validation_results[0].precision))

        plt.plot([elt[0] for elt in xys], [elt[1] for elt in xys])
        plt.show()

    def plot_1NN_fisher_precisions(self):
        
        expr = Experiment(froze_shuffle=True)

        plt.figure("Fisher precision for different number of folds")
        plt.xlabel("number of folds")
        plt.ylabel("precision")

        xys = []
        for number_folds in xrange(2, 12, 1):
            cv = expr.experiment(FisherFold(number_folds, 14), threshold_up=0, number_folds=number_folds, debug=False)
            xys.append((number_folds, cv.validation_results[0].precision))

        plt.plot([elt[0] for elt in xys], [elt[1] for elt in xys])
        plt.show()


if __name__ == "__main__":
    print __file__
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
