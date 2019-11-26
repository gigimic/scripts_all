# Refer the following
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# Python version
import sys
# print('Python: {}'.format(sys.version))
# scipy
import scipy
# print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
# print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
# print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
# print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
# print('sklearn: {}'.format(sklearn.__version__))
import csv

# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
print(len(dataset))
data1 = dataset.values
nn=len(data1)
# with open('iris_data.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(data1)
# csvFile.close()

# shape
print(dataset.shape)

# class distribution
print(dataset.groupby('class').size())
types = dataset.groupby('class').groups.keys()

type_classes= [type for type in types]

data_class = [dataset.groupby('class').groups[type_class] for type_class in type_classes] 

# box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()


# head
# print(dataset.head(100))

ser = range(len(data_class[0]))
markers =['^', 'o', 's', 'x']
fig = pyplot.figure()
grid_no=221
for j in range(3):
	ax1 = fig.add_subplot(grid_no)
	for i in range(4):
		# ax1.scatter(ser, data1[kount*j:kount*(j+1),i], marker=markers[i], label = names[i])
		ax1.scatter(ser, data1[data_class[j],i], marker=markers[i], label = names[i])
		if (j == 0): pyplot.legend()
	grid_no+=1
pyplot.show()


# pyplot.subplot(224)
# y1c = data1[:,0]
# y2c = data1[:,1]
# y3c = data1[:,2]
# y4c = data1[:,3]
# nn = range(len(y1c))
# pyplot.scatter(nn, y1c, marker='^')
# pyplot.scatter(nn,y2c, marker='o')
# pyplot.scatter(nn,y3c, marker='s')
# pyplot.scatter(nn,y4c, marker='x')



# pyplot.show()

# descriptions
print(dataset.describe())


# # histograms
# dataset.hist()
# pyplot.show()

# scatter plot matrix
# scatter_matrix(dataset)
# pyplot.show()


# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.20, random_state=1)
print(len(X), len(Y), len(X_train), len(Y_train))

# # Test options and evaluation metric
# kfold = StratifiedKFold(n_splits=10, random_state=1)
# cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Compare Algorithms
# pyplot.boxplot(results, labels=names)
# pyplot.title('Algorithm Comparison')
# pyplot.show()