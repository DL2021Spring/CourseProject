import matplotlib.pyplot as plt
__author__ = 'Daniel'


class Plotter(object):
    def plot(self, L_lst):
        plt.figure("Log_likelihood")
        plt.ylabel("L: Log-likelihood")
        plt.xlabel("N: number of iterations")
        plt.plot([i+1 for i in xrange(len(L_lst))], L_lst)
        plt.show()
        

class Plotter2D(object):
    def label(self, name, x_label, y_label):
        plt.figure(name)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    def plot_line(self, x1, y1, x2, y2):
        plt.plot([x1, x2], [y1, y2])

    def plot_scatter(self, X, Y, color="b"):
        plt.scatter(X, Y, c=color)

    def show(self):
        plt.show() 
