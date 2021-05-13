














import logging

import cv2
from helper.common import *
from helper.video import *

import sys
sys.path.append("../..")

from facerec.model import PredictableModel
from facerec.feature import Fisherfaces
from facerec.distance import EuclideanDistance
from facerec.classifier import NearestNeighbor
from facerec.validation import KFoldCrossValidation
from facerec.serialization import save_model, load_model

from facedet.detector import CascadedDetector

class ExtendedPredictableModel(PredictableModel):
    

    def __init__(self, feature, classifier, image_size, subject_names):
        PredictableModel.__init__(self, feature=feature, classifier=classifier)
        self.image_size = image_size
        self.subject_names = subject_names

def get_model(image_size, subject_names):
    
    
    feature = Fisherfaces()
    
    classifier = NearestNeighbor(dist_metric=EuclideanDistance(), k=1)
    
    return ExtendedPredictableModel(feature=feature, classifier=classifier, image_size=image_size, subject_names=subject_names)

def read_subject_names(path):
    
    folder_names = []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            folder_names.append(subdirname)
    return folder_names

def read_images(path, image_size=None):
    
    c = 0
    X = []
    y = []
    folder_names = []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            folder_names.append(subdirname)
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                    
                    if (image_size is not None):
                        im = cv2.resize(im, image_size)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            c = c+1
    return [X,y,folder_names]


class App(object):
    def __init__(self, model, camera_id, cascade_filename):
        self.model = model
        self.detector = CascadedDetector(cascade_fn=cascade_filename, minNeighbors=5, scaleFactor=1.1)
        self.cam = create_capture(camera_id)
            
    def run(self):
        while True:
            ret, frame = self.cam.read()
            
            img = cv2.resize(frame, (frame.shape[1]/2, frame.shape[0]/2), interpolation = cv2.INTER_CUBIC)
            imgout = img.copy()
            for i,r in enumerate(self.detector.detect(img)):
                x0,y0,x1,y1 = r
                
                face = img[y0:y1, x0:x1]
                face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                face = cv2.resize(face, self.model.image_size, interpolation = cv2.INTER_CUBIC)
                
                prediction = self.model.predict(face)[0]
                
                cv2.rectangle(imgout, (x0,y0),(x1,y1),(0,255,0),2)
                
                draw_str(imgout, (x0-20,y0-20), self.model.subject_names[prediction])
            cv2.imshow('videofacerec', imgout)
            
            ch = cv2.waitKey(10)
            if ch == 27:
                break

if __name__ == '__main__':
    from optparse import OptionParser
    
    
    
    usage = "usage: %prog [options] model_filename"
    
    parser = OptionParser(usage=usage)
    parser.add_option("-r", "--resize", action="store", type="string", dest="size", default="100x100", 
        help="Resizes the given dataset to a given size in format [width]x[height] (default: 100x100).")
    parser.add_option("-v", "--validate", action="store", dest="numfolds", type="int", default=None, 
        help="Performs a k-fold cross validation on the dataset, if given (default: None).")
    parser.add_option("-t", "--train", action="store", dest="dataset", type="string", default=None,
        help="Trains the model on the given dataset.")
    parser.add_option("-i", "--id", action="store", dest="camera_id", type="int", default=0, 
        help="Sets the Camera Id to be used (default: 0).")
    parser.add_option("-c", "--cascade", action="store", dest="cascade_filename", default="haarcascade_frontalface_alt2.xml",
        help="Sets the path to the Haar Cascade used for the face detection part (default: haarcascade_frontalface_alt2.xml).")
    
    parser.print_help()
    print "Press [ESC] to exit the program!"
    print "Script output:"
    
    (options, args) = parser.parse_args()
    
    if len(args) == 0:
        print "[Error] No prediction model was given."
        sys.exit()
    
    model_filename = args[0]
    
    if (options.dataset is None) and (not os.path.exists(model_filename)):
        print "[Error] No prediction model found at '%s'." % model_filename
        sys.exit()
    
    if not os.path.exists(options.cascade_filename):
        print "[Error] No Cascade File found at '%s'." % options.cascade_filename
        sys.exit()
    
    
    
    
    try:
        image_size = (int(options.size.split("x")[0]), int(options.size.split("x")[1]))
    except:
        print "[Error] Unable to parse the given image size '%s'. Please pass it in the format [width]x[height]!" % options.size
        sys.exit()
    
    if options.dataset:
        
        if not os.path.exists(options.dataset):
            print "[Error] No dataset found at '%s'." % dataset_path
            sys.exit()    
        
        
        print "Loading dataset..."
        [images, labels, subject_names] = read_images(options.dataset, image_size)
        
        list_of_labels = list(xrange(max(labels)+1))
        subject_dictionary = dict(zip(list_of_labels, subject_names))
        
        model = get_model(image_size=image_size, subject_names=subject_dictionary)
        
        
        
        if options.numfolds:
            print "Validating model with %s folds..." % options.numfolds
            
            
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            
            logger = logging.getLogger("facerec")
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
            
            crossval = KFoldCrossValidation(model, k=options.numfolds)
            crossval.validate(images, labels)
            crossval.print_results()
        
        print "Computing the model..."
        model.compute(images, labels)
        
        print "Saving the model..."
        save_model(model_filename, model)
    else:
        print "Loading the model..."
        model = load_model(model_filename)
    
    
    if not isinstance(model, ExtendedPredictableModel):
        print "[Error] The given model is not of type '%s'." % "ExtendedPredictableModel"
        sys.exit()
    
    
    print "Starting application..."
    App(model=model,
        camera_id=options.camera_id,
        cascade_filename=options.cascade_filename).run()
