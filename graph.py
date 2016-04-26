import numpy as np
import matplotlib.pyplot as plt
negative_matrix = []
positive_matrix = []

def graph(feature, target):
    j = 0
    for i in target:
        if i == 0:
            negative_matrix.append(feature[j].tolist())
        else:
            positive_matrix.append(feature[j].tolist())
        j += 1
    print()
    plt.scatter(np.asarray(positive_matrix)[:,0][:,1], np.asarray(positive_matrix)[:,0][:,2], label = 'hello', color = "r")
    plt.scatter(np.asarray(negative_matrix)[:, 0][:, 1], np.asarray(negative_matrix)[:, 0][:, 2], label = 'world', color="b")
    plt.legend(loc='upper right', shadow=True)
    #plt.show()