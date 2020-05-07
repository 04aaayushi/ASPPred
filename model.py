import pickle
import pandas as pd
from sklearn.model_selection import RepeatedKFold
from sklearn.ensemble import RandomForestClassifier

data_train = pd.read_csv('76+197train.csv')
data_test = pd.read_csv('76+197test.csv')

data_train1 = data_train.copy()
data_test1 = data_test.copy()

data_train1.isnull()
data_test1.isnull()

data_train1.drop([217, 218, 219], axis=0, inplace=True)
data_train1 = data_train1.dropna(axis=1)

features = ['CHARGE', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
features1 = ['CHARGE', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

y = data_train1['label'].values
test_y = data_test1['label'].values
x = data_train1[features].values
test_x = data_test1[features1].values

kf = RepeatedKFold(n_splits=5, n_repeats=150, random_state=10)
x_test = x_train = y_train = y_test = 0
for train_index, test_index in kf.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]

model = RandomForestClassifier(n_estimators=250, random_state=123)
model.fit(x_train, y_train)
ypred = model.predict(x_test)
# Saving model to disk
pickle.dump(model, open('model.pkl', 'wb'))
