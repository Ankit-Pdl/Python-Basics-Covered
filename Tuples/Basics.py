# students = [1,2,3]
# students[0] = 12
# print(students)

# students = (1,2,3)
# print(type(students))

# students = ("Anamika",)
# print(type(students))

# adding

#! tuple -> list-> operations->  tuple->copy

# number = (1,2,3,4,5)
# temp = list(number)
# temp.append(6)
# temp.remove(1)
# temp = tuple(temp)
# number = temp
# print(number)

# number = (1,2,3,4,5)
# for x in number:
#     print(x)

# ! why tuple? 

# ! speed 

import timeit
print("Lists: ", timeit.timeit(stmt="['Anamika']",number=100000000))
print("Tuple: ", timeit.timeit(stmt="('Anamika',)",number=100000000))

