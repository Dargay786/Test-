

students_list =[]
students_dict = {} #{"Tshering":"Student","Dargay":"Teacher"}

name  = input("Enter your name: ")
age = int(input("Your age: "))
grade = int(input("Your grade: "))

students_list.append(name)
students_dict[name] = {"Age":age, "Grade":grade}

print("Student added successfully!")
print(students_dict.items())
print()
print()

search_student = input("Ente rname of the student to search: ")
if search_student in students_list:
    print("Student found.")
    print(f"student details: Name:{name} Age:{age} Grade: {grade}")
else:
    print("student not Found")

remove_student = input("Enter the name of the student to remove")
if remove_student in students_list:
    removeage = students_dict[remove_student]
    removegrade = students_dict[remove_student]
    students_list.remove(remove_student)
    del students_dict[remove_student]
    print("student removed")
else:
    print("no student is found !")

