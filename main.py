class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f" Студенты: " "\n" f" Имя: {self.name}" "\n" f" Фамилия: {self.surname}" "\n" f" Курсы в процессе изучения: {self.courses_in_progress}" "\n" f" Завершенные курсы: {self.finished_courses}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f" Лекторы: " "\n" f" Имя: {self.name}" "\n" f" Фамилия: {self.surname}"


class Reviewer(Mentor):

    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f" Проверяющие: " "\n" f" Имя: {self.name}" "\n" f" Фамилия: {self.surname}"


best_student = Student('Roy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.add_courses('Introduction')

worst_student = Student('Emma', 'Loyd', 'female' )
worst_student.courses_in_progress += ['Python']

reviewer_one = Reviewer('George', 'Potter')
reviewer_one.courses_attached += ['Python']

lecturer_one = Lecturer('Michael', 'Snape')
lecturer_one.courses_attached += ['Python']

reviewer_one.rate_homework(best_student, 'Python', 10)
reviewer_one.rate_homework(best_student, 'Python', 8)
reviewer_one.rate_homework(worst_student, 'Python', 5)
reviewer_one.rate_homework(worst_student, 'Python', 3)

worst_student.rate_lecturer(lecturer_one, 'Python', 8)

print(best_student)
print(lecturer_one)
print(reviewer_one)

print(best_student.grades)
print(lecturer_one.grades)

