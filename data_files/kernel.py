


import numpy as np


class Kernel:
    def __init__(self, alpha, gammas):
        self.alpha = np.exp(alpha)
        self.gammas = np.exp(gammas)
        self.dim = gammas.size
        self.nparams = self.dim + 1

    def set_params(self, params):
        assert params.size == self.nparams
        self.alpha = np.exp(params).copy().flatten()[0]
        self.gammas = np.exp(params).copy().flatten()[1:]

    def get_params(self):
        
        return np.log(np.hstack((self.alpha, self.gammas)))

    def __call__(self, x1, x2):
        
        if x1.size / len(x1) == 1:
            N1 = 1
            D1 = x1.size
        else:
            N1, D1 = x1.shape
        if x2.size / len(x2) == 1:
            N2 = 1
            D2 = x2.size
        else:
            N2, D2 = x2.shape
        assert D1 == D2, "x1 dimension not equal to x2"
        assert D1 == self.dim, "data dimension not equal to the kernel"
        diff = x1.reshape(N1, 1, D1) - x2.reshape(1, N2, D2)
        diff = self.alpha * np.exp(-np.sum(np.square(diff) * self.gammas, -1) / 2)
        
        return diff

    def gradients(self, x1):
        
        N1, D1 = x1.shape
        diff = x1.reshape(N1, 1, D1) - x1.reshape(1, N1, D1)
        sqdiff = np.sum(np.square(diff) * self.gammas, -1)
        expdiff = np.exp(-sqdiff / 2)
        
        grads = [-0.5 * g * np.square(diff[:, :, i]) * self.alpha * expdiff for i, g in enumerate(self.gammas)]
        
        grads.insert(0, self.alpha * expdiff)
        return grads

    def gradients_wrt_data(self, x1, indexn=None, indexd=None):
        
        N1, D1 = x1.shape
        diff = x1.reshape(N1, 1, D1) - x1.reshape(1, N1, D1)
        sqdiff = np.sum(np.square(diff) * self.gammas, -1)
        expdiff = np.exp(-sqdiff / 2)
        

        rslt = []

        if (indexn is None) and (indexd is None):
            for n in range(N1):
                for d in range(D1):
                    K = np.zeros((N1, N1))
                    K[n, :] = -self.alpha * expdiff[n, :] * self.gammas[d] * (x1[n, d] - x1[:, d])
                    
                    K[:, n] = K[n, :]
                    rslt.append(K.copy())
            return rslt

        else:
            K = np.zeros((N1, N1))
            K[indexn, :] = -self.alpha * self.gammas[indexd] * (x1[indexn, indexd] - x1[:, indexd]) * expdiff[indexn, :]
            K[:, indexn] = K[indexn, :]
            return K.copy()