import numpy as np
import math
def compute_cost(feature):
    theta = np.zeros((np.shape(feature)[0], 1))
    result_theta = theta.transpose() * feature
    return sigmoid_function(result_theta)


def sigmoid_function(theta):

    denom = 1+ np.power(math.e ,-theta)
    return 1/denom

