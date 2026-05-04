 
# * Problem of the Day!!
#? You have this list of students:
#* students = [ "Ankit", "Sita", "Ram", "Priya" ]

#! Your task — write code to do all of these:

#? 1. Add "Bikash" to the end of the list

#? 2. Remove "Ram" from the list

#? 3. Sort the list alphabetically

#? 4. Print the total number of students

#? Expected output
#? ['Ankit', 'Bikash', 'Priya', 'Sita']
#? Total students: 4

students = [ "Ankit", "Sita", "Ram", "Priya" ]
students.append("Bikash")
print(students)
students.remove("Ram")
print(students)
# sorting
students.sort()
print(students)

print(len(students))