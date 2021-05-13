

import os

from LBP import *
import cv2
import pickle
from util.commons_util.logger_utils.Timer import Timer
from multiprocessing import Pool


radius = 1

nei = 8

scale = 4

scale_step = 1.25

winsize = int((25 - 1) / 2)

stride = 2



orl_path = 'E:/GPforFR/data/orl_faces'
lfw_path = 'E:/GPforFR/data/lfw_p'


orl_dst_path = 'E:/GPforFR/data/orl_faces_feature'
lfw_dst_path = 'E:/GPforFR/data/lfw_feature'

def extract_feature(args):
    timer = Timer()
    timer.start()

    img_path, ftr_name = args
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if not os.path.exists(os.path.dirname(ftr_name)):
        os.makedirs(os.path.dirname(ftr_name))
    out_file = open(ftr_name, 'w')
    feature = multi_scale_lbp_feature(image, radius, nei, scale, scale_step, winsize, stride)
    pickle.dump(feature, out_file)
    out_file.close()

    print timer.end()


def extract(dir_path, dst_path, include_folder_name=False):
    
    p = Pool(4)
    for root, dirs, files in os.walk(dir_path):
        if files:
            load = []
            for f in files:
                img_path = root + '/' + f
                folder = "" 
                if include_folder_name:
                    folder = root.replace('/', '/').split('/')[-1]+'_'
                ftr_name = os.path.join(dst_path, folder+f.split('.')[0] + '.txt')
                load.append((img_path, ftr_name))

            p.map(extract_feature, load)
            
        print root
    p.close()

if __name__=="__main__":
    extract(orl_path, orl_dst_path, True)
