# Data preprocessing

# Import library
import pandas as pd

# Import dataset
dataset = pd.read_csv('Data.csv')
#print dataset

# Create metric of feature
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values
print X
print Y