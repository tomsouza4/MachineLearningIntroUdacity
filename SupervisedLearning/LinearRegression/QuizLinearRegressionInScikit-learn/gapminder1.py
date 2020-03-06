# TODO: Add import statements
from sklearn.linear_model import LinearRegression
import pandas as pd

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv("LinearRegression/QuizLinearRegressionInScikit-learn/bmi_and_life_expectancy.csv") 


# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data['BMI'].values.reshape(-1,1),bmi_life_data['Life expectancy'].values.reshape(-1,1))
#print(bmi_life_data.head())

# Make a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict([[21.07931]])
print("Well done, your prediction of a life expectancy {} is correct!".format(laos_life_exp))
