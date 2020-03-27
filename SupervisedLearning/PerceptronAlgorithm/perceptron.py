import numpy as np
"""
For a point with coordinates (p,q), label y, and prediction 
given by the equation (y hat) ÿ=step(w1​x1 + w2​x2​ + b):
    If the point is correctly classified, do nothing.
    If the point is classified positive, but it has a negative label, subtract αp, αq, and α 
    from w1, w2, and b respectively.
    If the point is classified negative, but it has a positive label, add αp,αq, and α to w1, w2, and b respectively
Then click on test run to graph the solution that the perceptron algorithm gives you. It'll actually draw a set of 
dotted lines, that show how the algorithm approaches to the best solution, given by the black solid line. 
"""

import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0
#This function calculates the y_hat y=step(w1​x1 + w2​x2​ + b)
def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):

    # Goes over Weights array - X
    for i in range(len(X)):
        pred = prediction(X[i],W,b)
        
        # if prediction is == 1
        print("pred: {}".format(pred))
        if y[i] - pred == 1:
            W[0] += learn_rate*X[i][0] #updates the weight W1
            W[1] += learn_rate*X[i][1] #updates the weight W2
            b += learn_rate #updates the bias
        # if prediction is == -1
        elif y[i] - pred == -1:
            W[0] -= learn_rate*X[i][0] #updates the weight W1
            W[1] -= learn_rate*X[i][1] #updates the weight W2
            b -= learn_rate #updates the bias
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 10):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    #print("x_min: {}".format(x_min))
    #print("x_max: {}".format(x_max))
    #print("y: {}".format(y))
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    #print("W: {}".format(W))
    #print("b: {}".format(b))
    #print("X: {}".format(X))
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines

