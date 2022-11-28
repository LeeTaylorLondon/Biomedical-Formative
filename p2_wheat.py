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
from sklearn.model_selection import train_test_split

X = data.drop(['type'], axis=1)
Y = data['type']

# Splitting the dataset into 80% training data and 20% testing data.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.20, random_state=0)

def mape(y_actual, y_predicted):
    return np.mean(np.abs((Y_actual - Y_Predicted)/Y_actual))*100

# Building the KNN Model on our dataset
from sklearn.neighbors import KNeighborsRegressor
KNN_model = KNeighborsRegressor(n_neighbors=3).fit(X_train,Y_train)
# Prediction
KNN_predict = KNN_model.predict(X_test) #Predictions on Testing data