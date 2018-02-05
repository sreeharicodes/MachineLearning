#
#--------------- A Simple Decision Tree Implementation
#
#---------------  using scikit Learn

from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
# create data frame containing your data, each column can be accessed # by df['column   name']
df = pd.read_csv('t.csv')



et = DecisionTreeClassifier()

columns = ["Gender", "Age", "Salary","Married"]


labels = df["Default"].values
features = df[list(columns)].values

print labels

print features

et.fit(features,labels)

vect = [[0,50,100000,0]]


n = et.predict(vect)

print n

