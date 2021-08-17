# In cross-validation, we run our modeling process on different subsets of the data to get 
# multiple measures of model quality.
# For example, we could begin by dividing the data into 5 pieces, each 20% of the full dataset. 
# In this case, we say that we have broken the data into 5 "folds".
# we divide the dataset into 5 sets. Run the model with one of this set as the validation dataset. 
# Again run the model with the second set as the validation dataset. After we run the model for 5 times 
# we can decide on how the model can be used.

# cross-validation can be used for  small datasets, where extra computational burden isn't a big deal, 

# For larger datasets, a single validation set is sufficient. we may have enough data that 
# there's little need to re-use some of it for holdout.
# There's no simple threshold for what constitutes a large vs. small dataset. 
# But if your model takes a couple minutes or less to run, it's probably worth switching to cross-validation.

# We can run cross-validation and see if the scores for each experiment seem close. 
# If each experiment yields the same results, a single validation set is probably sufficient.

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                             ])

# We obtain the cross-validation scores with the cross_val_score() function from scikit-learn. 
# We set the number of folds with the cv parameter.
from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')

print("MAE scores:\n", scores)
print("Average MAE score (across experiments):")
print(scores.mean())

# Using cross-validation yields a much better measure of model quality, 
# with the added benefit of cleaning up our code: note that we no longer need 
# to keep track of separate training and validation sets. So, especially for 
# small datasets, it's a good improvement!

