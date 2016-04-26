from load_csv import loadMatrices
from hypothesis_function import hypothesis
from cost_function import compute_cost
from graph import graph

feature, target = loadMatrices()
theta = hypothesis(feature)
graph(feature,target)


