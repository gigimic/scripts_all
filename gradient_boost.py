# Gradient boosting is a method that goes through cycles to iteratively add models into an ensemble.
# It begins by initializing the ensemble with a single model
# then add more models to the ensemble to improve the results
# XGboost (extreme gradient boosting) library is used to do such method

from xgboost import XGBRegressor

my_model = XGBRegressor()
my_model.fit(X_train, y_train)

# make predictions and evaluate the model
from sklearn.metrics import mean_absolute_error

predictions = my_model.predict(X_valid)
print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))

# parameter tuning
# n_estimators specifies how many times to go through the modeling cycle. 
# It is equal to the number of models that we include in the ensemble.
# Typical values range from 100-1000, though this depends a lot on the learning_rate parameter 
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train)


# early_stopping_rounds offers a way to automatically find the ideal value for n_estimators. 
# Early stopping causes the model to stop iterating when the validation score stops improving, 
# even if we aren't at the hard stop for n_estimators. 

# Since random chance sometimes causes a single round where validation scores don't improve, 
# you need to specify a number for how many rounds of straight deterioration to allow before stopping. 
# Setting early_stopping_rounds=5 is a reasonable choice. In this case, we stop after 5 straight 
# rounds of deteriorating validation scores.

# When using early_stopping_rounds, you also need to set aside some data for calculating 
# the validation scores - this is done by setting the eval_set parameter.
my_model = XGBRegressor(n_estimators=500)
my_model.fit(X_train, y_train, 
             early_stopping_rounds=5, 
             eval_set=[(X_valid, y_valid)],
             verbose=False)

# learning_rate: Instead of getting predictions by simply adding up the predictions from each component 
# model, we can multiply the predictions from each model by a small number (known as the learning rate) 
# before adding them in.

# This means each tree we add to the ensemble helps us less. So, we can set a higher value for 
# n_estimators without overfitting. If we use early stopping, the appropriate number of trees 
# will be determined automatically.

# In general, a small learning rate and large number of estimators will yield more accurate 
# XGBoost models, though it will also take the model longer to train since it does more 
# iterations through the cycle. As default, XGBoost sets learning_rate=0.1.

my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
my_model.fit(X_train, y_train, 
             early_stopping_rounds=5, 
             eval_set=[(X_valid, y_valid)], 
             verbose=False)

# n_jobs: On larger datasets where runtime is a consideration, you can use parallelism 
# to build your models faster. It's common to set the parameter n_jobs equal to the number of 
# cores on your machine. On smaller datasets, this won't help.

my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
my_model.fit(X_train, y_train, 
             early_stopping_rounds=5, 
             eval_set=[(X_valid, y_valid)], 
             verbose=False)
    
# exercise 
import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X = pd.read_csv('../input/train.csv', index_col='Id')
X_test_full = pd.read_csv('../input/test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X.SalePrice              
X.drop(['SalePrice'], axis=1, inplace=True)

# Break off validation set from training data
X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                                random_state=0)

# "Cardinality" means the number of unique values in a column
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
low_cardinality_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and 
                        X_train_full[cname].dtype == "object"]

# Select numeric columns
numeric_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# Keep selected columns only
my_cols = low_cardinality_cols + numeric_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()
X_test = X_test_full[my_cols].copy()

# One-hot encode the data (we use pandas)
X_train = pd.get_dummies(X_train)
X_valid = pd.get_dummies(X_valid)
X_test = pd.get_dummies(X_test)
X_train, X_valid = X_train.align(X_valid, join='left', axis=1)
X_train, X_test = X_train.align(X_test, join='left', axis=1)


