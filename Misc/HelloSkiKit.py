from sklearn import datasets
import numpy as np

boston = datasets.load_boston()
print boston.DESCR #output omitted due to length

housing = datasets.fetch_california_housing()

print housing.DESCR #output omitted due to length
