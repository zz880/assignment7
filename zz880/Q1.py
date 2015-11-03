import numpy as np

def question1():
    # Create a 2D array X
    X = np.arange(1,16,1).reshape((5,3),order="F")

    # New array contains 2nd and 4th rows of X
    X1 = X[(1,3),:]
    print 'Question 1a: \n', X1

    # New array contains 2nd column of X
    X2 = X[:,1]
    print 'Question 1b: \n', X2
    
    # A new array contains all the elements in the rectangular section between the coordinates  [1,0] and  [3,2]
    X3 = []
    for i in range(1,4):
        for j in range(i-1,3):
            X3.append(X[i][j])
    print 'Question 1c: \n', X3

    # A new array that contains only elements with values that are between 3 and 11
    X4 = X[np.logical_and(X>=3, X<=11)]
    print 'Question 1d: \n', X4