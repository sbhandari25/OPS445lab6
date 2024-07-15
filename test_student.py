from lab6a import Student

# Create a new student instance
student1 = Student('Jack', '931686102')

# Add grades and display information
student1.addGrade('ops535', 2.0)
student1.addGrade('win310', 0.0)

print(student1.displayStudent())
print(student1.displayGPA())
print(student1.displayCourses())

