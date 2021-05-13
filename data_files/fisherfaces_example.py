import sys

sys.path.append("../..")

from facerec.dataset import DataSet
from facerec.feature import Fisherfaces
from facerec.distance import EuclideanDistance, CosineDistance
from facerec.classifier import NearestNeighbor
from facerec.classifier import SVM
from facerec.model import PredictableModel
from facerec.validation import KFoldCrossValidation
from facerec.visual import subplot
from facerec.util import minmax_normalize

import numpy as np

import matplotlib.cm as cm

import logging,sys

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger("facerec")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

dataSet = DataSet("/home/philipp/facerec/data/yalefaces_recognition")

feature = Fisherfaces()

classifier = NearestNeighbor(dist_metric=EuclideanDistance(), k=1)

model = PredictableModel(feature=feature, classifier=classifier)

model.compute(dataSet.data, dataSet.labels)


E = []
for i in xrange(min(model.feature.eigenvectors.shape[1], 16)):
    e = model.feature.eigenvectors[:,i].reshape(dataSet.data[0].shape)
    E.append(minmax_normalize(e,0,255, dtype=np.uint8))

subplot(title="Fisherfaces", images=E, rows=4, cols=4, sptitle="Fisherface", colormap=cm.jet, filename="fisherfaces.pdf")

cv = KFoldCrossValidation(model, k=10)
cv.validate(dataSet.data, dataSet.labels)
cv.print_results()
