#Prerequisite torch installation required
#If torch is not recognized: Ctrl+Shift+P --> Python Interpreter 

import torch
import numpy as np
print(f"Torch verison: {torch.__version__}")

#Initalizing Tensors
#Directly creating data
tensor_1D = torch.tensor([3,2]) 
tensor_2D = torch.tensor([[3,2]])

#From a NumPy array
np_array = np.array([1,2])

#Constant & Random Valuesgit push origin main

dimension = (2,3)
random_tuple = torch.rand(dimension)
ones_tuple = torch.ones(dimension)

#Attributes of a Tensor (Shape, Datatype, Device which stored on)
print("\nTensor Shape: ", {tensor_1D.shape})
print("Datatype: ", {tensor_1D.dtype})
print("Device Stored In: ", {tensor_1D.device})

#Tensor Operations 

 #Index and Slicing 
tensor_test = torch.rand(4,5) #2D Tensor with (4 rows, 5 columns)
print(tensor_test) 
print(f"First row: {tensor_test[0]}")
print(f"First column: {tensor_test[:,0]}") #: referring to all elements in dimension row
print(f"Last column: {tensor_test[...,-1]}") #... move through all dimensions; stop at specified index 

 #Concatenate Tensors
tensor2 = torch.tensor([3,3])
new_tensor = torch.cat([tensor_1D,tensor2])
print(f"Concatenate: {new_tensor}\n")

 #Arithmetic Operations
 #Most operations should run the same. 
  #Matrix Multiplication (2 ways)
tensor_array = torch.tensor([[2,3]]) 
print(tensor_2D @ tensor_array.T) #Using matrix multiplication symbol @ and .T to transpose a matrix.

print(torch.matmul(tensor_2D, tensor_array.T)) #Calling .matmul() function


#Tensors are defaulted to the cpu. To move tensors to an accelerator (ex. CUDA), the .to method 
#can be used. Copying large tensors across devices can cost a lot of time & memory. 
 #Checks if moving to accelerator is available
if torch.accelerator.is_available():
    tensor = tensor_1D.to(torch.accelerator.current_accelerator())
    print("Device Stored In: ", {tensor.device})
else:
    print("Not available")

