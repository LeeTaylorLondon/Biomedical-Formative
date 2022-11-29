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


''' 
classify wheat seed varieties to Kama, Rosa, 
and Canadian with kNN; plot the learning curves
(accuracy) for best k
'''

data = pd.read_csv("Data/wheat.csv")
corr_matrix = data.loc[:].corr()
print(corr_matrix)


''' WIP Drop highly correlated variables '''
pass


# Separating the dependent and independent data variables into two data frames.
X = data.drop(['type'], axis=1)
Y = data['type']

# Splitting the dataset into 80% training data and 20% testing data.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.20, random_state=0)


# n_neighbors = 3
# # y = np.sin(X).ravel()
# for i, weights in enumerate(["uniform", "distance"]):
#     knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
#     y_ = knn.fit(X_train, Y_train).predict(X_test)
#     plt.subplot(2, 1, i + 1)
#     print(X_train.shape, Y_train.shape)
#     # plt.scatter(X_test, Y_test, color="darkorange", label="data")
#     plt.plot(X_test, y_, color="navy", label="prediction")
#     plt.axis("tight")
#     plt.legend()
#     plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors, weights))
# plt.tight_layout()
# plt.show()


def model_fit():
    def mape(y_actual, y_predicted):
        return np.mean(np.abs((y_actual - y_predicted)/y_actual))*100

    # Building the KNN Model on our dataset
    KNN_model = KNeighborsRegressor(n_neighbors=3).fit(X_train, Y_train)
    # Prediction
    KNN_predict = KNN_model.predict(X_test)  # Predictions on Testing data

    plt.plot(KNN_predict, Y_test)
    plt.show()

    # Using MAPE error metrics to check for the error rate and accuracy level
    KNN_MAPE = mape(Y_test, KNN_predict)
    Accuracy_KNN = 100 - KNN_MAPE
    print("MAPE: ", KNN_MAPE)
    print('Accuracy of KNN model: {:0.2f}%.'.format(Accuracy_KNN))


if __name__ == '__main__':
    model_fit()