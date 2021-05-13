

import pickle
import numpy as np
import os.path
import numpy.matlib as mat


class Join_Ftr(object):
    def Join_feature(self, fl1, fl2):
        
        

        
        ftr1 = pickle.load(fl1)
        ftr2 = pickle.load(fl2)

        
        
        
        
        
        
        
        row, col = ftr1.shape
        jnt_ftr = np.empty([5, col * 2])
        for i in range(5):
            jnt_ftr[i] = np.append(ftr1[i], ftr2[i])
        
        
        
        return jnt_ftr

    def Constrct_XY(self, feature_pth, X_info):
        


        X = []
        Y = []

        for i in range(len(X_info)):
            pth1 = os.path.join(feature_pth, X_info[i][0])
            pth2 = os.path.join(feature_pth, X_info[i][1])
            if os.path.exists(pth1) and os.path.exists(pth2):
                fl1 = open(pth1, 'r')
                fl2 = open(pth2, 'r')

                X.append(self.Join_feature(fl1, fl2))
                Y.append(X_info[i][2])
                fl1.close()
                fl2.close()

        return X, Y

    def XY_in(self, X, Y):
        
        assert len(X) == len(Y), "the number of the image pair and their corresponding y is not equal"
        num_of_pair = len(X)
        num_of_patch = X[0].shape[0]
        n_ftr = X[0].shape[1]
        X_in = mat.zeros([num_of_pair * num_of_patch * 2, n_ftr])
        Y_in = mat.zeros([num_of_pair * num_of_patch * 2, 1])
        num = 0
        for i in range(num_of_pair):
            img_pair = X[i]
            for j in range(num_of_patch):
                X_in[num] = img_pair[j]
                Y_in[num] = Y[i]
                num = num + 1
                X_in[num, 0:n_ftr / 2] = img_pair[j][n_ftr / 2:]
                X_in[num, n_ftr / 2:] = img_pair[j][0:n_ftr / 2]
                Y_in[num] = Y[i]
                num = num + 1

        return X_in, Y_in
    
