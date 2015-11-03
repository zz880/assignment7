import numpy as np

def question3():
    X = np.random.rand(10,3)
    rank = np.argsort(abs(X-0.5))
    output = [X[i][np.where(rank[i,:]==0)][0] for i in range(10)]
    print 'Question 3: \n', output
