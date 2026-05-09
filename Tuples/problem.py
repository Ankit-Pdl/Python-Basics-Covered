# Problem Statement
# You are given a list of marks:

# marks = [85, 90, 78, 92, 88]

# Tasks:
#!Convert the list into a tuple called marks_tuple

#!Try to sort the tuple using .sort()

#! Observe what happens
# Convert the tuple back into a list
# Sort the list

#: Convert it back into a tuple
# Print the final sorted tuple+


marks = [85, 90, 78, 92, 88]
marks_tuple = tuple(marks)
print(type(marks_tuple))
#! marks_tuple.sort() Error!
marks = list(marks_tuple)
marks.sort()
marks_tuple = tuple(marks)
print(marks_tuple)

myset = {1,2,3,1,3}
print(myset)






