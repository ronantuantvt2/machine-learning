# Data preprocessing

# Import library
import pandas as pd

# Import dataset
dataset = pd.read_csv('Data.csv')
# print dataset

# Create metric of feature
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values
# print X
# print Y

# Taking care of missing data
# Using imputer library of sklearn to handle this issue
# Doc: http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Imputer.html
from sklearn.preprocessing import Imputer
# Determine which one is missing
missingValues = 'NaN' 
# How process missing data
# mean : using average along the axis
# median: 
# most_frequent: using the most frequent value along the axis
strategy = 'mean'
# axis column: 0, row: 1 , default: 0
axis = 0
imputer = Imputer(missingValues, strategy, axis)
# fit imputer object to dataset
# take all column index 1,2
imputer = imputer.fit(X[:, 1:3])
# Replace data by the mean of column
X[:, 1:3] = imputer.transform(X[:, 1:3])
print X