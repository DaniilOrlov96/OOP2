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

    def __lt__(self, other, course):
        if not isinstance(other, Student) and course in self.courses_in_progress:
            print('Это не студент!')
            return
        std_grades = self.grades[course]
        sum = 0
        for i in std_grades:
            sum += i
            average_grade_1 = (sum / len(self.grades[course]))
        oth_grades = other.grades[course]
        sum = 0
        for i in oth_grades:
            sum += i
            average_grade_2 = (sum / len(other.grades[course]))
        return print(average_grade_1 < average_grade_2)

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

    def __lt__(self, other, course):
        if not isinstance(other, Lecturer) and course in self.courses_attached:
            print('Это не лектор!')
            return
        lec_grades = self.grades[course]
        sum = 0
        for i in lec_grades:
            sum += i
            average_grade_1 = (sum / len(self.grades[course]))
        oth_grades = other.grades[course]
        sum = 0
        for i in oth_grades:
            sum += i
            average_grade_2 = (sum / len(other.grades[course]))
        return print(average_grade_1 < average_grade_2)

    def __str__(self):
        return f" Лекторы: " "\n" f" Имя: {self.name}" "\n" f" Фамилия: {self.surname}" "\n"


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


def average_lecturer_grade (lecturer_list, Python):
    lecturers_grades = lecturer_one.grades['Python'] + lecturer_two.grades['Python']
    sum = 0
    for i in lecturers_grades:
        sum += i
        all_lecturers_avr_grade = (sum / len(lecturers_grades))
    return print(f" Средняя оценка лекторов за курс:", all_lecturers_avr_grade)


average_lecturer_grade(lecturer_list, 'Python')

reviewer_one.rate_homework(best_student, 'Python', 10)
reviewer_one.rate_homework(best_student, 'Python', 8)
reviewer_one.rate_homework(worst_student, 'Python', 5)
reviewer_one.rate_homework(worst_student, 'Python', 3)


def average_homework_grade (student_list, Python):
    students_grades = best_student.grades['Python'] + worst_student.grades['Python']
    sum = 0
    for i in students_grades:
        sum += i
        all_students_avr_grade = (sum / len(students_grades))
    return print(f" Средняя оценка студентов за курс:", all_students_avr_grade)


average_homework_grade(student_list, 'Python')

best_student.__lt__(worst_student, 'Python')
lecturer_two.__lt__(lecturer_one, 'Python')

print(best_student)
print(lecturer_one)
print(reviewer_one)



