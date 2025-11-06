#program to take srn of some students in dictionary and marks of 5 subjects and display the total marks

n=input("Enter srn of students and marks seperated by space and comma between two diff srn: ")
details_split = n.split(",")  # Split the srn into parts
student_marks = {}
for detail in details_split:
    parts = detail.strip().split()
    srn = parts[0]
    marks = list(map(int, parts[1:]))
    student_marks[srn] = marks
for srn, marks in student_marks.items():
    total = sum(marks)
    print(f"Total marks of student {srn} is {total}")