class Kernel(object):
    def apply(self, **kwargs):
        raise NotImplementedError("Not implemented")


class QuadraticKernel(Kernel):
    def apply(self, X, Y, x):
        ret = np.dot(X.T, x)
        ret += 1
        ret = np.power(ret, 2)

        d, T = x.shape
        ret = np.multiply(ret, np.repeat(Y[:, np.newaxis], repeats=T, axis=1))
        ret = np.sum(ret, axis=0)
        return ret

class RbfKernel(Kernel):
    def __init__(self, sigma):
        self.sigma = sigma
        super(RbfKernel, self).__init__()

    def apply(self, X, Y, x):
        d, T = x.shape
        _, N = X.shape
        ret = np.zeros((N, T))
        for i in xrange(T):
            point = x[:, i]
            cur = X - np.repeat(point[:, np.newaxis], repeats=N, axis=1)
            cur = np.linalg.norm(cur, axis=0)
            cur = -np.power(cur, 2)
            cur = np.exp(cur/(2*self.sigma**2))
            cur = np.multiply(cur, Y)
            ret[:, i] = cur

        ret = np.sum(ret, axis=0)
        return ret
