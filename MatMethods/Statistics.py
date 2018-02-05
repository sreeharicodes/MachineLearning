import re, math, random # regexes, math functions, random numbers

import matplotlib.pyplot as plt # pyplot

from collections import defaultdict, Counter

from functools import partial
from collections import Counter


def dot(v, w):
   
    return sum(v_i * w_i for v_i, w_i in zip(v, w))




def sum_of_squares(v):
       
    return dot(v, v)

def mean(x): 
    
    return sum(x) / len(x)





def median(v):
   
   n = len(v)
    
   sorted_v = sorted(v)
    
   midpoint = n // 2
    
    
   if n % 2 == 1:
        # if odd, return the middle value
 
       return sorted_v[midpoint]
   
   else:
        # if even, return the average of the middle values
       
       lo = midpoint - 1
        
       hi = midpoint
        
       return (sorted_v[lo] + sorted_v[hi]) / 2
   

def quantile(x, p):
    
    p_index = int(p * len(x))
    
    return sorted(x)[p_index]

def mode(x):
    
     counts = Counter(x)
    
     max_count = max(counts.values())
    
     return [x_i for x_i, count in counts.iteritems()
 if count == max_count]

def data_range(x):
    
    return max(x) - min(x)



def de_mean(x):
    
    x_bar = mean(x)
   
    return [x_i - x_bar for x_i in x]

def variance(x):
    
    n = len(x)
    
    deviations = de_mean(x)
    
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x):
    
    return math.sqrt(variance(x))



def interquartile_range(x):
   
    return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x, y):
   
    n = len(x)
    
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    
    stdev_x = standard_deviation(x)
    
    stdev_y = standard_deviation(y)
    
    if stdev_x > 0 and stdev_y > 0:
        
       return covariance(x, y) / stdev_x / stdev_y
   
    else:
        
       return 0 # if no variation, correlation is zero

if __name__ == '__main__':
	print "Hello World...."     