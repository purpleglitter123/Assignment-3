class Person:
 def __init__(self, name, id, contact_info):
 self.name = name
 self.id = id
 self.contact_info = contact_info
 def get_name(self):
 return self.name
 # ... other common methods for Person
class Student(Person):
 def __init__(self, major, enrollment_status, gpa, *args, **kwargs):
 super().__init__(*args, **kwargs) # Call Person's constructor
 self.major = major
 self.enrollment_status = enrollment_status
 self.gpa = gpa
 self.courses_taken = []
 def get_major(self):
 return self.major
 # ... other methods for Student
 def take_course(self, course):
 # Check prerequisites, add course to student's list, update course enrollment
 # ... implementation details
 def calculate_gpa(self):
 # Calculate GPA based on grades in courses_taken
 # ... implementation details
class Professor(Person):
 def __init__(self, department, *args, **kwargs):
 super().__init__(*args, **kwargs)
 self.department = department
 self.courses_taught = []
 def get_department(self):
 return self.department
 # ... other methods for Professor
 def create_course(self, course_name, credit_hours):
 # Create a new Course object and assign the professor
 # ... implementation details
 def grade_student(self, student, course, grade):
 # Add or update the student's grade in the course
 # ... implementation details
class Course:
 def __init__(self, name, id, professor, credit_hours):
 self.name = name
 self.id = id
 self.professor = professor
 self.enrolled_students = []
 self.credit_hours = credit_hours
 def get_name(self):
 return self.name
 # ... other methods for Course
class UndergraduateCourse(Course):
 # ... additional attributes and methods for undergraduate courses
class GraduateCourse(Course):
 # ... additional attributes and methods for graduate courses