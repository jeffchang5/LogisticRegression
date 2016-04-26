import numpy as np
import math
def hypothesis(feature):
    m, n = np.shape(feature)
    theta = np.zeros((m, 1))
    print(theta)
    result_theta = theta.transpose() * feature
    return sigmoid_function(result_theta)


def sigmoid_function(theta):
    denom = 1+ np.power(math.e ,-theta)
    print(1/denom)
    return 1/denom


