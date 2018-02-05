#---------------- Multiple Linear Regression Simple
#
#  X => { SlNo,Diameter,No of Topings }
#  Y => { Price in Dollars }

from numpy.linalg import inv
from numpy import dot, transpose
from numpy.linalg import lstsq

#----- We can read X from a file as well....
X = [[1, 6, 2], [1, 8, 1], [1, 10, 0], [1, 14, 2], [1, 18, 0]]

#-------------- Price in Dollars
y = [[7], [9], [13], [17.5], [18]]

#------------------------  (X*X^T)^-1

XtransDotX = inv(dot(transpose(X),X))

#------------------------- X^T * Y
XtransDotY = dot(transpose(X),y)

#---------------------- Weight = 

Weight = dot(XtransDotX, XtransDotY)


print Weight


print lstsq(X, y)[0]
