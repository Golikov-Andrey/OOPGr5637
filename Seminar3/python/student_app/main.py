from typing import List

from domain.student import Student
from domain.student_group import StudentGroup


s1 = Student("Иван", 25)
s2 = Student("Игорь", 23)
s3 = Student("Иван", 22)
s4 = Student("Игорь", 23)
s5 = Student("Даша", 23)
s6 = Student("Лена", 23)

list_stud = [s1, s2, s3, s4, s5, s6]

group4580 = StudentGroup(list_stud, 4580)
print(group4580)    

for std in group4580:
    print(std)

print("=========================================================")

# sorted_group = sorted(group4580.getGroup(), key=lambda student: student.age)
sorted_group = sorted(group4580.getGroup())

for std in sorted_group:
    print(std)