'''
Regularization Exercise
Perhaps it's not too surprising at this point, but there are classes in sklearn that will help you perform 
regularization with your linear regression. You'll get practice with implementing that in this exercise. 
In this assignment's data.csv, you'll find data for a bunch of points including six predictor variables and 
one outcome variable. Use sklearn's Lasso class to fit a linear regression model to the data, while also using 
L1 regularization to control for model complexity.

Perform the following steps:
1. Load in the data
The data is in the file called 'data.csv'. Note that there's no header row on this file.
Split the data so that the six predictor features (first six columns) are stored in X, and the outcome 
feature (last column) is stored in y.

2. Fit data using linear regression with Lasso regularization
Create an instance of sklearn's Lasso class and assign it to the variable lasso_reg. You don't need to set any parameter 
values: use the default values for the quiz.
Use the Lasso object's .fit() method to fit the regression model onto the data.

3. Inspect the coefficients of the regression model
Obtain the coefficients of the fit regression model using the .coef_ attribute of the Lasso object. Store this in 
the reg_coef variable: the coefficients will be printed out, and you will use your observations to answer the question 
at the bottom of the page.
regularization.py
'''
# TODO: Add import statements
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
import pandas as pd

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv('LinearRegression/QuizRegularization/data.csv', header=None)
X = train_data.iloc[:,0:6]
y = train_data.iloc[:,-1]

# TODO: Create the linear regression model with lasso regularization.
#model = LinearRegression()
lasso_reg = Lasso(alpha=1.0)
#lasso_reg = LinearRegression()

# TODO: Fit the model.
lasso_reg.fit(X, y)

# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)

'''
Coeficient using Lasso
[ 0.          2.35793224  2.00441646 -0.05511954 -3.92808318  0.        ]

Lasso regularization has set the coefficients for the first and sixth columns to 0. 
You might try fitting the model to a standard LinearRegression, to see what those 
coefficients were before regularization!

Coeficient using Linear Regression
[-6.19918532e-03  2.96325160e+00  1.98199191e+00 -7.86249920e-02 -3.95818772e+00  9.30786141e+00]
 '''