import numpy as np

# arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
# b = arr1[3:]
# print(b)
# b[0] = 35
# print(b)
# print(arr1)
# arr1[0] = 9

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)


# matrices
# matrix1 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [5, 6, 7, 8]])
# print(matrix1.shape)
# print(matrix1.ndim)
# print(matrix1.size)
# print(matrix1[1, 2])


# default matrices
# zeros_matrix = np.zeros(2)
# print(zeros_matrix)
#
# ones_matrix = np.ones(2, dtype=int)  # a la matriz se le puede indicar el tipo de datos, en este caso int
# for i in ones_matrix:
#     print(type(i))
# print(ones_matrix)
#
# empty_matrix = np.empty(3)
# print(empty_matrix)


# ranges
# range1 = np.arange(0, 5)
# print(range1)


# espacio lineal
# x = np.linspace(0, 10, 10)
# print(x)


# operaciones

# arr1 = np.array([2, 1, 5, 4, 3, 6, 7])
# print(np.sort(arr1))
# arr2 = np.array([0, 2, 3, 5, 3, 6, 8])
# arr3 = np.concatenate((arr1, arr2))
# print(arr3)

# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6]])
# z = np.concatenate((x, y), axis=0)
# print(z)

# Reshape a horizontal list a data
# a = np.arange(6)
# print(a)
# b = a.reshape(3, 2)
# print(b)

# sum
x = np.array([1, 2, 3])
y = np.array([3, 4, 5])
# print(x + y)

# scalar product
# print(3 * y)
