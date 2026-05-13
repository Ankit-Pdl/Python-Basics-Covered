
#! for while

#! for (tempVariable) in function, collection

# for i in range(1,11):
#     print(i)

# students = ["Anamika","Aayush","Samriddhi","Rahul","Shahrukh"]

# for i in range(5):
#     print(students[i])

# #! while condition

# age = 14

# # while age <=18:
    
# #     print(f'{age} minor')



# age =15
# while age<=18:
#     age +=1
    
#     if age == 17:
#         continue
#     print(f'{age} minor')
    


for i in range(1,51):
    
    if i % 3 == 0:    
        print("Fuzz")
        continue
    elif i% 5 ==0:
        print("Buzz")
        continue
    else:
        print(i)
