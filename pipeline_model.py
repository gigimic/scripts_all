# Pipelines are a simple way to keep the data preprocessing and modeling code organized. 
# Specifically, a pipeline bundles preprocessing and modeling steps so we can use 
# the whole bundle as if it were a single step.
# Some important benefits are:
# Cleaner Code: Accounting for data at each step of preprocessing can get messy. 
# With a pipeline, you won't need to manually keep track of your training and 
# validation data at each step.
# Fewer Bugs: There are fewer opportunities to misapply a step or forget a preprocessing step.
# Easier to Productionize: It can be surprisingly hard to transition a model from a prototype 
# to something deployable at scale. Pipelines can help.
# More Options for Model Validation:
# The following example use the ColumnTransformer class to bundle together 
# different preprocessing steps
# The following assumptions are made: 1)Imputed the missing numerical values, 
# 2) imputed missing values and applied one-hot-encoding to missng categorical data

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='constant')

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# define the model
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=0)

# With the pipeline, we preprocess the training data and fit the model in a single line of code. 
# With the pipeline, we supply the unprocessed features in X_valid to the predict() command, 
# and the pipeline automatically preprocesses the features before generating predictions. 

from sklearn.metrics import mean_absolute_error

# Bundle preprocessing and modeling code in a pipeline
my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('model', model)
                             ])

# Preprocessing of training data, fit model 
my_pipeline.fit(X_train, y_train)

# Preprocessing of validation data, get predictions
preds = my_pipeline.predict(X_valid)

# Evaluate the model
score = mean_absolute_error(y_valid, preds)
print('MAE:', score)

