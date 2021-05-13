
































import cStringIO
import base64

try:
    from PIL import Image
except ImportError:
    import Image


from flask import Flask, request, request_finished, json, abort, make_response, Response, jsonify


import sys
sys.path.append("../../..")
from facerec.model import PredictableModel
from facerec.lbp import ExtendedLBP
from facerec.feature import SpatialHistogram
from facerec.distance import ChiSquareDistance
from facerec.classifier import NearestNeighbor


import logging
from logging.handlers import RotatingFileHandler


import recognition


app = Flask(__name__)










IMAGE_DECODE_ERROR = 10
IMAGE_RESIZE_ERROR = 11
PREDICTION_ERROR = 12
SERVICE_TEMPORARY_UNAVAILABLE = 20
UNKNOWN_ERROR = 21
INVALID_FORMAT = 30
INVALID_API_KEY = 31
INVALID_API_TOKEN = 32
MISSING_ARGUMENTS = 40

errors = {
    IMAGE_DECODE_ERROR : "IMAGE_DECODE_ERROR",
    IMAGE_RESIZE_ERROR  : "IMAGE_RESIZE_ERROR",
    SERVICE_TEMPORARY_UNAVAILABLE	: "SERVICE_TEMPORARILY_UNAVAILABLE",
    PREDICTION_ERROR : "PREDICTION_ERROR",
    UNKNOWN_ERROR : "UNKNOWN_ERROR",
    INVALID_FORMAT : "INVALID_FORMAT",
    INVALID_API_KEY : "INVALID_API_KEY",
    INVALID_API_TOKEN : "INVALID_API_TOKEN",
    MISSING_ARGUMENTS : "MISSING_ARGUMENTS"
}




LOG_FILENAME = 'serverlog.log'
LOG_BACKUP_COUNT = 5
LOG_FILE_SIZE_BYTES = 50 * 1024 * 1024

def init_logger(app):
    handler = RotatingFileHandler(LOG_FILENAME, maxBytes=LOG_FILE_SIZE_BYTES, backupCount=LOG_BACKUP_COUNT)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    loggers = [app.logger, logging.getLogger('facerec')]
    for logger in loggers:
        logger.addHandler(handler)








def init_app(app):
    init_logger(app)

init_app(app)

@app.before_request
def log_request():
    app.logger.debug("Request: %s %s", request.method, request.url)
    



class WebAppException(Exception):

    def __init__(self, error_code, exception, status_code=None):
        Exception.__init__(self)
        self.status_code = 400
        self.exception = exception
        self.error_code = error_code
        try:
            self.message = errors[self.error_code]
        except:
            self.error_code = UNKNOWN_ERROR
            self.message = errors[self.error_code]
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = dict()
        rv['status'] = 'failed'
        rv['code'] = self.error_code
        rv['message'] = self.message
        return rv





class ThrowsWebAppException(object):
   def __init__(self, error_code, status_code=None):
      self.error_code = error_code
      self.status_code = status_code

   def __call__(self, function):
      def returnfunction(*args, **kwargs):
         try:
            return function(*args, **kwargs)
         except Exception as e:
            raise WebAppException(self.error_code, e)
      return returnfunction





@app.errorhandler(WebAppException)
def handle_exception(error):
    app.logger.exception(error.exception)
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response




@ThrowsWebAppException(error_code = IMAGE_DECODE_ERROR)
def read_image(base64_image):
    
    enc_data = base64.b64decode(base64_image)
    file_like = cStringIO.StringIO(enc_data)
    im = Image.open(file_like)
    im = im.convert("L")
    return im

def preprocess_image(image_data):
    image = read_image(image_data)
    return image


@ThrowsWebAppException(error_code = PREDICTION_ERROR)
def get_prediction(image_data):
    image = preprocess_image(image_data)
    prediction = model.predict(image)
    return prediction




@app.route('/api/recognize', methods=['GET', 'POST'])
def identify():
    if request.headers['Content-Type'] == 'application/json':
            try:
                image_data = request.json['image']
            except:
                raise WebAppException(error_code=MISSING_ARGUMENTS)
            prediction = get_prediction(image_data)
            response = jsonify(name = prediction) 
            return response
    else:
        raise WebAppException(error_code=INVALID_FORMAT)


if __name__ == '__main__':
    
    long_description = ("server.py is a simple facerec webservice. It provides "
        "you with a simple RESTful API to recognize faces from a "
        "computed model. Please don't use this server in a production "
        "environment, as it provides no security and there might be "
        "ugly concurrency issues with the global state of the model." )
    print "=== Description ==="
    print long_description
    
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-t", "--train", action="store", dest="dataset", default=None, 
        help="Calculates a new model from a given CSV file. CSV format: <person>;</path/to/image/folder>.", required=False)
    parser.add_argument("-a", "--address", action="store", dest="host", default="0.0.0.0", 
        help="Sets the endpoint for this server.", required=False)
    parser.add_argument("-p", "--port", action="store", dest="port", default=5000, 
        help="Sets the port for this server.", required=False)
    parser.add_argument('model_filename', nargs='?', help="Filename of the model to use or store")
    
    print "=== Usage ==="
    parser.print_help()
    
    args = parser.parse_args()
    
    global model
    
    if args.dataset:
        
        model = recognition.get_model_from_csv(filename=args.dataset,out_model_filename=args.model_filename)
    else:
        model = recognition.load_model_file(args.model_filename)
    
    print "=== Server Log (also in %s) ===" % (LOG_FILENAME)
    app.run(host=args.host, port=args.port, debug=True, use_reloader=False, threaded=False)
