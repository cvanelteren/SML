import numpy as np
from scipy.stats import multivariate_normal as mv
from pylab import *


def kernel_function(x, theta):
    '''
    Code for equation 3
    '''

    sigma = np.zeros((len(x), len(x)))
    for idx, i in enumerate(x):
        for jdx, j in enumerate(x):
            sigma[idx, jdx] = \
            theta[0] * np.exp(- .5 * theta[1] * (i -  j)**2 ) + \
             theta[2] + theta[3] * i * j
    return sigma



# number of points to sample
N = 101
x = np.linspace(-1, 1, N)
theta = [1,1,1,1]
K = kernel_function(x, theta)

mu = np.zeros(len(x))
# for some reason it erros on singularity?
prior = mv(mu, K, allow_singular = 1)
samples = prior.rvs(5)

fig, ax = subplots(1,1)
for i in samples:
    ax.plot(x, i)
savefig('../Figures/ex_1_test')
show(block = 1)
