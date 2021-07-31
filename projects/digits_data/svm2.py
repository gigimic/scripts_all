import pandas as pd

# Kaggle data is used here 
# SVM model with kernel = 'rbf' is used to predict the digits

dig_data = pd.read_csv('train.csv')
df = pd.DataFrame(dig_data)

print(df.shape)
print(df.head())
# print(df.describe())
print(df['label'].unique())

X_train = df.drop('label', axis = 'columns')
y_train = df['label']
print(len(X_train), len(y_train))

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

linear_model = SVC(kernel = 'linear')

linear_model.fit(X_train,y_train)
print('training score ....', linear_model.score(X_train, y_train))

X_test = pd.read_csv('test.csv')
y_pred = linear_model.predict(X_test)

index_num = [x for x in range(1,len(y_pred)+1)]
df_out = pd.DataFrame({'ImageId': index_num, 'Label': y_pred})
df_out.to_csv('digit_predict_linear.csv', header=True, index = False) 
