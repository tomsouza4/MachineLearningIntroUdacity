import numpy as np
"""
Output expected:
Trying for L=[5,6,7].
The correct answer is
[0.09003057317038046, 0.24472847105479764, 0.6652409557748219]
"""


#create a random list of numbers
list_elem = list(np.random.rand(3))
soft_max = list()
# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    #L = [5,6,7] #to test the function
    L = np.exp(L) #Softmax function will exponentialize all the items in this list
    print(len(L)) #How big is this list?
    
    for i in range(len(L)):
        soft_max.append(L[i] / sum(L))
    
    #print(soft_max) #Show me the elements in this list
    
    return soft_max #return the list with all the softmax calculation
    