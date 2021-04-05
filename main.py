class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = []

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
        self.courses_in_progress = ",".join(self.courses_in_progress)
        self.finished_courses = ",".join(self.finished_courses)
        return f" Студенты: " "\n" f" Имя: {self.name}" "\n" f" Фамилия: {self.surname}" "\n" f" Средняя оценка за домашние задания: {self.average_grade} " "\n" f" Курсы в процессе изучения: {self.courses_in_progress}" "\n" f" Завершенные курсы: {self.finished_courses}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        std_grades = self.grades['Python']
        sum = 0
        for i in std_grades:
            sum += i
            self.average_grade = (sum / len(self.grades['Python']))
        oth_grades = other.grades['Python']
        sum = 0
        for i in oth_grades:
            sum += i
            other.average_grade = (sum / len(other.grades['Python']))
        return print(self.average_grade < other.average_grade)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.courses_attached = []
        self.average_grade = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        lec_grades = self.grades['Python']
        sum = 0
        for i in lec_grades:
            sum += i
            self.average_grade = (sum / len(self.grades['Python']))
        oth_grades = other.grades['Python']
        sum = 0
        for i in oth_grades:
            sum += i
            other.average_grade = (sum / len(other.grades['Python']))
        return print(self.average_grade < other.average_grade)

    def __str__(self):
        return f" Лекторы: " "\n" f" Имя: {self.name}" "\n" f" Фамилия: {self.surname}" "\n" f" Средняя оценка за домашние задания: {self.average_grade} " "\n"


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

student_list = [best_student, worst_student]

reviewer_one = Reviewer('George', 'Potter')
reviewer_one.courses_attached += ['Python']

lecturer_one = Lecturer('Michael', 'Snape')
lecturer_one.courses_attached += ['Python']

lecturer_two = Lecturer('Alan', 'Waker')
lecturer_two.courses_attached += ['Python']

lecturer_list = [lecturer_one, lecturer_two]

best_student.rate_lecturer(lecturer_two, 'Python', 7)
best_student.rate_lecturer(lecturer_one, 'Python', 9)
worst_student.rate_lecturer(lecturer_two, 'Python', 5)
worst_student.rate_lecturer(lecturer_one, 'Python', 8)


def average_lecturer_grade(lecturer_list, course_name):
    lecturer_list = lecturer_one.grades[course_name] + lecturer_two.grades[course_name]
    sum = 0
    for lecturer in lecturer_list:
        sum += lecturer
        all_lecturers_avr_grade = (sum / len(lecturer_list))
    return print(f" Средняя оценка лекторов за курс:", all_lecturers_avr_grade)


average_lecturer_grade(lecturer_list, 'Python')

reviewer_one.rate_homework(best_student, 'Python', 10)
reviewer_one.rate_homework(best_student, 'Python', 8)
reviewer_one.rate_homework(worst_student, 'Python', 5)
reviewer_one.rate_homework(worst_student, 'Python', 3)


def average_homework_grade(student_list, course_name):
    student_list = best_student.grades[course_name] + worst_student.grades[course_name]
    sum = 0
    for student in student_list:
        sum += student
        all_students_avr_grade = (sum / len(student_list))
    return print(f" Средняя оценка студентов за курс:", all_students_avr_grade)


average_homework_grade(student_list, 'Python')

worst_student < best_student

lecturer_one < lecturer_two

print(best_student)
print(lecturer_one)
print(reviewer_one)



