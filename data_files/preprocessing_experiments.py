
































import sys, os
sys.path.append("../..")

from facerec.feature import Fisherfaces, PCA, SpatialHistogram, Identity
from facerec.distance import EuclideanDistance, ChiSquareDistance
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
from facerec.validation import KFoldCrossValidation
from facerec.visual import subplot
from facerec.util import minmax_normalize
from facerec.serialization import save_model, load_model

import numpy as np

try:
    from PIL import Image
except ImportError:
    import Image
import matplotlib.cm as cm
import logging
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from facerec.lbp import LPQ, ExtendedLBP

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
        
        azimuth = int(filename[12:16])
        elevation = int(filename[17:20])

        
        if azimuth < self._min_azimuth or azimuth > self._max_azimuth:
            return False
        if elevation < self._min_elevation or elevation > self._max_elevation:
            return False
            
        return True

def read_images(path, fileNameFilter=FileNameFilter("None"), sz=None):
    
    c = 0
    X,y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                if fileNameFilter(filename):
                    print filename
                    try:
                        im = Image.open(os.path.join(subject_path, filename))
                        im = im.convert("L")
                        
                        if (sz is not None):
                            im = im.resize(self.sz, Image.ANTIALIAS)
                        X.append(np.asarray(im, dtype=np.uint8))
                        y.append(c)
                    except IOError, (errno, strerror):
                        print "I/O error({0}): {1}".format(errno, strerror)
                    except:
                        print "Unexpected error:", sys.exc_info()[0]
                        raise
            c = c+1
    return [X,y]


if __name__ == "__main__":
    
    
    out_dir = None
    
    
    
    if len(sys.argv) < 2:
        print "USAGE: facerec_demo.py </path/to/images>"
        sys.exit()
    yale_filter = YaleBaseFilter(-25, 25, -25, 25)
    
    [X,y] = read_images(sys.argv[1], yale_filter)
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger = logging.getLogger("facerec")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    feature = PCA()
    
    classifier = NearestNeighbor(dist_metric=EuclideanDistance(), k=1)
    
    model = PredictableModel(feature=feature, classifier=classifier)
    
    model.compute(X, y)
    
    
    E = []
    for i in xrange(min(model.feature.eigenvectors.shape[1], 16)):
        e = model.feature.eigenvectors[:,i].reshape(X[0].shape)
        E.append(minmax_normalize(e,0,255, dtype=np.uint8))
    
    subplot(title="Fisherfaces", images=E, rows=4, cols=4, sptitle="Fisherface", colormap=cm.jet, filename="fisherfaces.png")
    
    cv = KFoldCrossValidation(model, k=10)
    cv.validate(X, y)
    
    cv.print_results()
