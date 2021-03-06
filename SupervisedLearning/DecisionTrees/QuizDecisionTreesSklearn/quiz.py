'''
Decision Tree Quiz
In this quiz, you'll be given the following sample dataset, and your goal is to define a model that gives 100% accuracy 
on it.

The data file can be found under the "data.csv" tab in the quiz below. It includes three columns, the first 2 
comprising of the coordinates of the points, and the third one of the label.

The data will be loaded for you, and split into features X and labels y.

You'll need to complete each of the following steps:

1. Build a decision tree model
Create a decision tree classification model using scikit-learn's DecisionTreeClassifier and assign it to the 
variablemodel.

2. Fit the model to the data
You won't need to specify any of the hyperparameters, since the default ones will yield a model that perfectly classifies 
the training data. However, we encourage you to play with hyperparameters such as max_depth and min_samples_leaf to try 
to find the simplest possible model.

3. Predict using the model
Predict the labels for the training set, and assign this list to the variable y_pred.

4. Calculate the accuracy of the model
For this, use the function sklearn function accuracy_score. A model's accuracy is the fraction of all data points that it 
correctly classified.
When you hit Test Run, you'll be able to see the boundary region of your model, which will help you tune the correct 
parameters, in case you need them.

Note: This quiz requires you to find an accuracy of 100% on the training set. This is like memorizing the training data! 
A model designed to have 100% accuracy on training data is unlikely to generalize well to new data. If you pick very large
values for your parameters, the model will fit the training set very well, but may not generalize well. Try to find the 
smallest possible parameters that do the job—then the model will be more likely to generalize well. 
(This aspect of the exercise won't be graded.)
'''

# Import statements 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO 
import pydotplus
import pandas as pd
import numpy as np

# Read the data.
data = np.asarray(pd.read_csv('DecisionTrees/QuizDecisionTreesSklearn/data.csv', header=None))
# Assign the features to the variable X, and the labels to the variable y. 
X = data[:,0:2]
y = data[:,2]
feature_cols = ['X', 'Y']

# TODO: Create the decision tree model and assign it to the variable model.
# You won't need to, but if you'd like, play with hyperparameters such
# as max_depth and min_samples_leaf and see what they do to the decision
# boundary.
#model = DecisionTreeClassifier(max_depth=,min_samples_leaf=)
model = DecisionTreeClassifier(criterion="entropy")

# TODO: Fit the model.
model.fit(X,y)

# TODO: Make predictions. Store them in the variable y_pred.
y_pred = model.predict(X)

# TODO: Calculate the accuracy and assign it to the variable acc.
acc = accuracy_score(y,y_pred)
print("Accuracy of this model: {}".format(acc))

dot_data = StringIO()
export_graphviz(model, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True, 
                feature_names = feature_cols, class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('DecisionTrees/QuizDecisionTreesSklearn/prediction_decision_tree.png')
