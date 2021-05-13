import cv2
import numpy as np
__author__ = 'Daniel'


def imshow(mat, img_name="Image Name"):
    
    cv2.imshow(img_name, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def random_img(size=(400, 400)):
    
    mat = np.random.randint(0, 255, size)
    mat = np.asarray(mat, dtype=np.int8)
    return mat


def blurred_img(size=(400, 400)):
    
    mat = random_img(size)
    kernel = cv2.getGaussianKernel(129, 7)
    mat = cv2.filter2D(mat, cv2.CV_8UC3, kernel)  
    mat = np.asarray(mat, dtype=np.int8)
    return mat


if __name__ == "__main__":
    imshow(random_img())
    imshow(blurred_img())