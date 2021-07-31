import pandas as pd
from sklearn.datasets import load_digits
dig_data = load_digits()
print(dir(dig_data))
print(dig_data.target_names)

df = pd.DataFrame(dig_data.data)
df['target'] = dig_data.target
print(df.head())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis = 'columns'), df.target, test_size = 0.3)

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

# using rbf kernel

rbf_model = SVC(kernel = 'rbf')
print(len(X_train), len(X_test))

rbf_model.fit(X_train,y_train)
print('training score ....', rbf_model.score(X_train, y_train))
print('test score ... ', rbf_model.score(X_test, y_test))
y_pred = rbf_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
f1score = f1_score(y_test, y_pred, average ='micro')

print('confusiotn matrix..\n',cm)
print('accuracy... ', acc)
print('Fi score...  ', f1score)


# using linear kernel

linear_model = SVC(kernel = 'linear')
print(len(X_train), len(X_test))

linear_model.fit(X_train,y_train)
print('training score ....', linear_model.score(X_train, y_train))
print('test score ... ', linear_model.score(X_test, y_test))