'''
Polynomial Regression Exercise
Get some practice implementing polynomial regression in this exercise. In data.csv, you can see data generated 
for one predictor feature ('Var_X') and one outcome feature ('Var_Y'), following a non-linear trend. 
Use sklearn's PolynomialFeatures class to extend the predictor feature column into multiple columns with polynomial 
features. Play around with different degrees of polynomial and the Test Run button to see what fits best: when you 
think you have the best-fitting degree, press the Submit button to check your work!

Perform the following steps below:
1. Load in the data
The data is in the file called 'data.csv'. Note that this data has a header line.
Make sure that you've split out the data into the predictor feature in X and outcome feature in y.
For X, make sure it is in a 2-d array of 20 rows by 1 column. You might need to use NumPy's reshape function 
to accomplish this.

2. Create polynomial features
Create an instance of sklearn's PolynomialFeatures class and assign it to the variable poly_feat. Pay attention to 
how to set the degree of features, since that will be how the exercise is evaluated.
Create the polynomial features by using the PolynomialFeatures object's .fit_transform() method. The "fit" side of 
the method considers how many features are needed in the output, and the "transform" side applies those considerations 
to the data provided to the method as an argument. Assign the new feature matrix to the X_poly variable.

3. Build a polynomial regression model
Create a polynomial regression model by combining sklearn's LinearRegression class with the polynomial features. 
Assign the fit model to poly_model.
'''

# TODO: Add import statements
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd

# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = pd.read_csv("LinearRegression/QuizPolynomialRegression/data.csv")
X = train_data['Var_X'].values.reshape(20,1)
y = train_data['Var_Y']

# Create polynomial features
# TODO: Create a PolynomialFeatures object, then fit and transform the predictor feature
# the param degree=4 makes it curve and follow the data instead of just creating a straight line
poly_feat = PolynomialFeatures(degree=4)
X_poly = poly_feat.fit_transform(X)
#print(X_poly)

# Make and fit the polynomial regression model
# TODO: Create a LinearRegression object and fit it to the polynomial predictor
# features
model = LinearRegression()
poly_model = model.fit(X_poly, y.values.reshape(-1,1))

# Once you've completed all of the steps, select Test Run to see your model
# predictions against the data, or select Submit Answer to check if the degree
# of the polynomial features is the same as ours!