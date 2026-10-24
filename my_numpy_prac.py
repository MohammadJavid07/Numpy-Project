import numpy as np
#Generate and print evenly spaced numbers using NumPy.
num = np.array([22,44,55,66,77,88])
print(num)

#to print the type of an obj
print(type(num))

#to show the dimensions or shape of an object
print(num.shape)

#to print the last element of array
print(num[-1])

#to create an array of Zeros
zero_array = np.zeros(6)
print(zero_array)

#to create an array between specific range using arange()
rang_arr = np.arange(11,20)
print(rang_arr)


#to create an array between specific range using arange() with steps between numbers
num_arr = np.arange(1,10, 0.5)
print(num_arr)


linsp_arr = np.linspace(5,90)
print(linsp_arr)