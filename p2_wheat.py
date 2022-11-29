import random
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from imports import *


def txt_to_csv():
    # Open text file
    with open('Data/wheat.txt', 'r') as f:
        lines = f.readlines()
    # Convert comma seperated data
    csv = ''
    for i, v in enumerate(lines[::]):
        lines[i] = lines[i].split()
    # Format csv data
    for line in lines:
        csv = csv + ','.join(line) + '\n'
        print(line)
    # Write to .csv file
    with open('Data/wheat.csv', 'w') as f:
        f.writelines(csv)


data = pd.read_csv("Data/wheat.csv")
# data = data.drop(['perimeter'], axis=1)
corr_matrix = data.loc[:].corr()
print(corr_matrix)


x = np.array(data['asymmetry_coefficient'])
y = np.array(data['type'])
X, Y = [], []
for elmx, elmy in zip(x, y):
    X.append([elmx])
    Y.append([elmy])
X = np.array(X)
Y = np.array(Y)
print(X.shape, Y.shape)


def model():
    model = KNeighborsRegressor(algorithm='auto', n_neighbors=2,
                                p=3, weights='uniform', n_jobs=8)
    return model

def fit(model):
    # Building the KNN Model on our dataset
    model.fit(X_train, Y_train)
    return model

def predict(KNN_model):
    # Prediction
    prediction = KNN_model.predict(X_test)  # Predictions on Testing data
    return prediction

def stats(model, X, Y, pred_y):
    score = model.score(X, Y)
    print(score)

    mse = mean_squared_error(Y, pred_y)
    print("Mean Squared Error:", mse)

    rmse = math.sqrt(mse)
    print("Root Mean Squared Error:", rmse)


if __name__ == '__main__':
    ''' 
    classify wheat seed varieties to Kama, Rosa, 
    and Canadian with kNN; plot the learning curves
    (accuracy) for best k
    '''

    m = model()
    m.fit(X, Y)
    p = m.predict(X)

    stats(m, X, Y, p)

    x_ax = range(len(X))
    plt.scatter(x_ax, y, s=5, color="blue", label="original")
    plt.plot(x_ax, p, lw=1.5, color="red", label="predicted")
    plt.legend()
    plt.show()
