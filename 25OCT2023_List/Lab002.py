squares = [1, 4, 9, 16, 25, 1]
# index = [0, 1, 2, 3, 4]
# rev_index = [-5, -4, -3, -2, -1]
print(squares[0])
print(len(squares))
print(squares.count(1)) #counts number of occurance of the value
print(squares.count(2))
print(squares[-1])


squares = [1, 4, 9, 16, 25, 1]  # List - This allow Duplicate
print(type(squares))
squares_tuple = (1, 4, 9, 16, 25, 1)
copy_square=squares.copy()
# squares_tuple[1] = 20   'tuple' object does not support item assignment
# print(squares_tuple)
#copy_squares_tuple=squares_tuple.copy() #error 'tuple' object has no attribute 'copy'
print(type(squares_tuple ))
print(squares_tuple)

squares = [1, 4, 9, 16, 25]
# index = [0, 1, 2, 3, 4, 5]
print(squares.pop(1)) # Pop will remove the index value
print(squares)
print(squares.remove(16)) # Remove the Value not the Index
#print(squares.pop(1)) # Remove the Value not the Index
print(squares)
print(squares.pop(1)) # Remove the Value not the Index
print(squares)