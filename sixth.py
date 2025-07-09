
def calculate_grade(marks):
    mark = sum(marks) // len(marks)
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    elif mark >= 50:
        return "E"
    else:
        return "F"
name = input("Enter student name: ")
marks = list(map(int, input("Enter marks separated by space: ").split()))
grade = calculate_grade(marks)
print(f"Student: {name}")
print(f"Marks: {marks}")
print(f"Average mark: {sum(marks)/len(marks)}")
print(f"Grade: {grade}")
