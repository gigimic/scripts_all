# Data leakage happens when the training data contains information about the target, 
# but similar data will not be available when the model is used for prediction. 
# This leads to high performance on the training set, but the model will perform poorly in production.

# In other words, leakage causes a model to look accurate until we start making decisions 
# with the model, and then the model becomes very inaccurate.

# There are two main types of leakage: target leakage and train-test contamination.

# Target leakage occurs when your predictors include data that will not be available 
# at the time we make predictions. It is important to think about target leakage 
# in terms of the timing or chronological order that data becomes available, 
# not merely whether a feature helps make good predictions.

# Train-Test Contamination: this type of leak occurs when we aren't careful to distinguish 
# training data from validation data.

# Validation is meant to be a measure of how the model does on data that it hasn't considered before. 
# We can corrupt this process in subtle ways if the validation data affects the preprocessing behavior. 
# This is sometimes called train-test contamination.

# If your validation is based on a simple train-test split, exclude the validation data 
# from any type of fitting, including the fitting of preprocessing steps. This is easier 
# if you use scikit-learn pipelines. When using cross-validation, it's even more critical that 
# we do your preprocessing inside the pipeline!

from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Since there is no preprocessing, we don't need a pipeline (used anyway as best practice!)
my_pipeline = make_pipeline(RandomForestClassifier(n_estimators=100))
cv_scores = cross_val_score(my_pipeline, X, y, 
                            cv=5,
                            scoring='accuracy')

print("Cross-validation accuracy: %f" % cv_scores.mean()) # here we get a high accuracy

# after removing the not so suitable features
# Drop leaky predictors from dataset
potential_leaks = ['expenditure', 'share', 'active', 'majorcards']
X2 = X.drop(potential_leaks, axis=1)

# Evaluate the model with leaky predictors removed
cv_scores = cross_val_score(my_pipeline, X2, y, 
                            cv=5,
                            scoring='accuracy')

print("Cross-val accuracy: %f" % cv_scores.mean()) # lower accuracy, but better model 
# leakage is a hard and subtle issue