def sort_students(student_list):
    # Sort the student list in descending order based on CGPA
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Define a student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Example usage:
# Create a list of student objects
students = [
    Student("Alice", "123", 3.8),
    Student("Bob", "456", 3.5),
    Student("Charlie", "789", 3.9),
]

# Sort the list of students by CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
