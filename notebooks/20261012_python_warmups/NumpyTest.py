import numpy as np
from numpy import random 
import seaborn as sns
import matplotlib.pyplot as plt

print(np.__version__) #(check np verison)

#Numpy ndarray using the array() function 
array_test = np.array([1,2,3,4,5,6,7,8,9,10])
print("ndarray:",array_test, end = "\n\n")

#ndarray dimensions 
array_scalar = np.array(3) #One input 
#Python list [] into array .arry([])
array1D = np.array(["a","b","c"]) #One vector input 
array2D = np.array([[1,2,3], [4,5,6]]) #Matrix -> Two vector input 
array3D = np.array([[[1,3], [5,7]], [[2,4],[6,8]]])

custom_dim = np.array([1,2,3,4], ndmin = 5)
#Checking array dimension <array>.ndim
print("Dimensions:",array3D.ndim, end = "\n\n")
print("Custom array:",custom_dim, end = "\n\n")

###############################################################
#Array Indexing & Negative Indexing for backward movement
print("0th index of array_test:",array_test[0]) # 1D array
#Accesses INDEX element in row 1, column 2
print("1st indexed array, 2nd index element of array2D:",array2D[1,2]) 

print("0th indexed array, 1st index array, index 1 element:", array3D[0,1,1], end ="\n\n")
#Accesses first array, into the 2nd nested array and gets the 2nd element 

###############################################################
#Array Slicing [Begin:End:Step]
print(array_test[1:4], end = "\n\n") #Gets a subarray of elements
#including the beginning index but excluding the end index. 

#You can also omit values to include the rest of the left side
#or include the rest of the right side of the array, respectively.
print(array_test[:3])
print(array_test[0:])

#The third value, step, indicates how many steps the code takes, 
#and returning values where it briefly stops. 
#Starts at value 1, takes two step, gets 3, takes 2 more steps, gets 5, etc.
print(array_test[0:7:2], end = "\n\n") 

#Array Methods .copy() & .view()
#.copy() creates a completely separate array object from the original. 
# Changes made within one will not affect the other. 
arr_copy = array_test.copy()

#.view() creates a synced array object with the original. 
#Changes made in one will affect the other. 
arr_view = array_test.view()

#Joining Arrays
#Joining 1D Arrays
#notice for 1D arrays, it requires an additonal set of parentheses. 
#concatenate() expects all arrays to be in one collection (order matters).
joined_1D = np.concatenate((array1D,array_test))
print("1D joined arrays:",joined_1D)

#Joining 2D Arrays 
#array2D -> [[1,2,3], [4,5,6]]
abc2D = np.array([["x","y","z"],["a","b","c"]])
joined_2D = np.concatenate((array2D,abc2D),axis=1)
print("2D joined arrays (by axis 1):",joined_2D, end="\n\n")

#Joining with stack()
stack_array = np.stack((array2D,abc2D), axis=0)
print("2D stacked array:",stack_array)


#Creating Binomial Distributions 
binomial_dist = random.binomial(n=10,p=0.5,size=100)

#Plotting
sns.displot(binomial_dist)
plt.show()