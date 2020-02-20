import numpy as np
import matplotlib.pyplot as plt
import csv

'''
This code was created to be compared with batch_graddesc, and explan to myself how Gradient Descent
works, on that one it doesn't seem to tell me why it's not using RMSE formula to caulculate the cost

Code copied from https://gist.github.com/sagarmainkar/41d135a04d7d3bc4098f0664fe20cf3c
For sake of machine learning I can express the equation for a line in terms of machine learning in a different way. 
I would call y as my hypothesis and represent it as J(theta) and call b as theta0 and m as theta1. 
I can write same equation as : J(theta) = theta0 + theta1*X
To solve for the Theta0 and Theta1 analytical way I would have to write the following program:
theta_best = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

Well here is the analogy with machine learning terms now:
    Size of Steps took in any direction = Learning rate
    Gadget tells you height = Cost function
    The direction of your steps = Gradients

'''

def  cal_cost(X,y,theta=1):
    '''
    Calculates the cost for given X and Y. The following shows and example of a single dimensional X
    theta = Vector of thetas 
    X     = Row of X's np.zeros((2,j))
    y     = Actual y's np.zeros((2,1))
    where:
        j is the no of features
    MSE Cost formula
    '''
    
    m = len(y)
    predictions = X.dot(theta)
    #print("Predictions: {}".format(predictions[0][0]))
    cost = (1/2*m) * np.sum(np.square(predictions-y))
    #print("cost: {}".format(cost))
    return cost

def miniBatchGD(X, y, theta, batch_size = 20, learn_rate = 0.005, num_iter = 25):    
#def  miniBatchGD(X, y,          batch_size = 20, learn_rate = 0.005, num_iter = 25):
    '''
    X    = Matrix of X without added bias units
    y    = Vector of Y
    theta=Vector of thetas np.random.randn(j,1)
    learn_rate 
    num_iter = no of iterations
    
    Returns the final theta vector and array of cost history over no of iterations
    '''
    m = len(y)
    cost_history = np.zeros(num_iter)
    
    n_points = X.shape[0]
    
    cost = 0.0
        
    for it in range(num_iter):
        #Choose randomly the positions of the matrix like [40 60 95 66 56 3 41 91 5 32 19 14 6 28 35 84 80 65 90 5]
        batch = np.random.choice(range(n_points), batch_size)

        #According to the Random positions it select the coordinate X
        X_batch = X[batch,:]
        #According to the Random positions it select the coordinate y
        y_batch = y[batch]            

        #np.c_ Stacks 1-D arrays as columns into a 2-D array, it'll put back the coordinates X and y together
        X_batch = np.c_[np.ones(len(X_batch)),X_batch]

        #Multiplies matrices X_batch to the theta(which was generated randomly)
        prediction_theta = np.dot(X_batch,theta)
        #print("prediction_theta: {}".format(prediction_theta))
        #print("batch: {}".format(X_batch))
        #exit()

        #Gradient Formula
        theta = theta - (1/m)*learn_rate*(X_batch.T.dot((prediction_theta - y_batch)))
        
        #Cost
        cost += cal_cost(theta,X_batch,y_batch)
        
        #regression_coef.append(np.hstack((theta,cost)))
        #print("theta: ", theta)
        cost_history[it]  = cost
        #cost_history_formula[it]  = cost_formula

        #print("{};{}".format(cost_history[it], cost_history_formula[it]))    


    #return     
    return theta, cost_history

if __name__ == "__main__":
    #
    data = np.loadtxt('LinearRegression/QuizMiniBatchGradientDescent/data.csv', delimiter = ',')
    X = data[:,:-1]
    y = data[:,-1]
        
    theta = np.random.randn(2,1)
    #print("X: {}, y: {}, theta: {}".format(X,y,theta))
    theta,cost_history = miniBatchGD(X,y,theta)
    
    print('Theta0:          {:0.3f},\nTheta1:          {:0.3f}'.format(theta[0][0],theta[1][0]))
    print('Final cost/MSE:  {:0.3f}'.format(cost_history[-1]))     