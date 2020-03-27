import numpy as np

"""
Output Expected:
Trying for Y=[1,0,1,1] and P=[0.4,0.6,0.1,0.5].
The correct answer is: 4.8283137373
Mathmatical Formula: - sum( yiln(p_ith) + (1-y_ith)*ln(1-p_ith))
Where _ith is the ith element like 1 ith, 2 ith ... n ith
Solution proposed by Udacity: -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
"""

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    
    results = 0
    
    #Goes through the array of elements Y
    for i in range(len(Y)):
        results += Y[i]*np.log(P[i]) + (1-Y[i])*np.log(1-P[i]) #Generates a negative output
        print("results: {}".format(results))
    
    #Transform the natural log result into positive
    return results * -1