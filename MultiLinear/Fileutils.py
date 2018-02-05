import csv
import os
from numpy import *


def ReadFile( pfilename , pdirectory ):
	filename = pfilename
	directory = '.'  # <-- if you have linux or osx
	# directory = r'c:\some\directory'  # <-- if windows, the r is important
	# directory = 'c:/some/directory'  # <-- if windows (alternative)

	fullpath = os.path.join(directory, filename)

        verts = []
	with open(fullpath, 'r') as csvfile:
   		ofile = csv.reader(csvfile, delimiter=',')
    		# next(ofile) # <-- skip the x,y,z header

    		# this makes a generator of the remaining non-empty lines
    		rows = (r for r in ofile if r)

    		# this converts the string representation of each line
    		# to an x,y,z list, and stores it in the verts list.
    		verts = [[float(i) for i in r] for r in rows]


	return verts

# y = mx + b
# m is slope, b is y-intercept
def ComputeErrorForCurrentLine(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))


def GradientStep(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]


def ComputeGradientDescent(points, init_a, init_b, lr, n_iter):
    a = init_a
    b = init_b
    for i in range(n_iter):
        a, b = GradientStep(a, b, array(points), lr)
    return [a, b]


def EntryPoint():
    print "Hello World"
    points = genfromtxt('data.csv', delimiter=",")
    print points 
    LearningRate = 0.001
    NIterCount = 750
    Init_A = 0  # Y Intercept
    Init_B = 0  # Slope 
    [Final_A,Final_B] = ComputeGradientDescent( points,LearningRate,Init_A,Init_B,NIterCount)
    print Final_A
    print Final_B

if __name__ == '__main__':
    EntryPoint()
