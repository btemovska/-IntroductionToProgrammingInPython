class Student:
    def __init__(self, first, last, gpa):
        self.first = first # first name
        self.last = last   # last name
        self.gpa = gpa     # grade point average

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last

class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        # Your code goes here
        return len(self.roster)

if __name__ == "__main__":
    course = Course()

    course.add_student(Student('Henry', 'Bendel', 3.6))
    course.add_student(Student('Johnny', 'Moin', 2.9))

    print('Course size:', course.course_size())




