import csv
import numpy as np


def loadMatrices():
    feature_vector = []
    target_vector = []
    with open('ex2data2.txt') as file:
        field_names = ['test1', 'test2', 'accepted']
        reader = csv.DictReader(file, fieldnames= field_names)
        for row in reader:
            array = []
            array.append(1)
            array.append(float(row['test1']))
            array.append(float(row['test2']))
            feature_vector.append(array)
            target_vector.append(float(row['accepted']))
    return (np.asmatrix(feature_vector), target_vector)
