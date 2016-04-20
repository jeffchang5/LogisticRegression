import csv
import matplotlib
import numpy as np

feature_vector = []
target_vector = []

def hypothesis_function(m, theta, target):
    results = theta - target
    results = np.square(results)
    print(results)
    # print(np.shape(results))
    # print((1/(2 * m)) * results)

with open('data.csv') as file:
    field_names = ['house_size', 'no_of_rooms', 'house_price']
    reader = csv.DictReader(file, fieldnames= field_names)
    for row in reader:
        array = []
        array.append(float(row['house_size']))
        array.append(float(row['no_of_rooms']))
        feature_vector.append(array)
        target_vector.append([1, float(row['house_price'])])
feature_vector = np.asmatrix(feature_vector)
target_vector = np.asmatrix(target_vector)

m = feature_vector.shape[0]


hypothesis_function(m=m, theta=feature_vector,target=target_vector)

