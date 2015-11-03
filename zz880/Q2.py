import numpy as np

def question2():
    a = np.arange(25).reshape(5,5)
    b = np.array([1., 5, 10, 15, 20])[np.newaxis]
    c = []
    for i in range(0,5):
        c.append(a[:,i]/b)
    c = np.array(c).reshape((5,5)).T
    print 'Question 2: \n', c
