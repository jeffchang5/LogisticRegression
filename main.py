import csv
import matplotlib
import numpy as np
from load_csv import loadMatrices
from compute_cost import compute_cost

feature, target = loadMatrices()
print(compute_cost(feature))


