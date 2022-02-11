class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lect(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached 
            and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error' 
    
    def av_grade(self):
        sum_grades = 0
        for course, grades in self.grades.items():
            for grade in grades:
                sum_grades += grade
        return sum_grades / len(grades)
    
    def __str__(self):                                                         
        return f'{self.name}\n{self.surname}\nСредняя оценка за домашние задания: {self.av_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []        
    

class Reviewer(Mentor):                                                         
    def __init__(self, name, surname):  
        super().__init__(name, surname)  
    def rate_hw(self, student, course, grade):                                  
        if (isinstance(student, Student) and course in self.courses_attached
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка' 
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):                                                        
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}                                                        
    
    def av_grade(self):
        sum_grades = 0
        for course, grades in self.grades.items():
            for grade in grades:
                sum_grades += grade
        return sum_grades / len(grades)

    def __str__(self):
        return f'{self.name}\n{self.surname}\nСредняя оценка за лекции: {self.av_grade()}'

def rate_people(someone, somebody):
    a = someone.av_grade()
    b = somebody.av_grade()
    if a > b:
        print(f'Средняя оценка {someone.name} выше чем у {somebody.name}')
    elif a < b:
        print(f'Средняя оценка {somebody.name} выше чем у {someone.name}')
    else:
        print(f'Средняя оценка {someone.name} такая же как у {somebody.name}')

    

 
some_student = Student('Ruoy', 'Eman', 'Male')
some_student.courses_in_progress += ['Python','Git']
some_student.finished_courses += ['Введение в программирование']

worst_student = Student('Vasya', 'Pupkin', 'Male')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += []




some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

else_reviewer = Reviewer('No', 'Buddy')
else_reviewer.courses_attached += ['Python']


some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
else_lecturer = Lecturer('Any', 'Body')
else_lecturer.courses_attached += ['Python']


some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(worst_student, 'Python', 4)
else_reviewer.rate_hw(worst_student, 'Python', 5)
else_reviewer.rate_hw(some_student, 'Python', 10)



some_student.rate_lect(some_lecturer, 'Python', 8)
worst_student.rate_lect(some_lecturer, 'Python', 9)
some_student.rate_lect(else_lecturer, 'Python', 9)
worst_student.rate_lect(else_lecturer, 'Python', 10)



# print(best_student.name, best_student.surname)
# print(best_student.grades)
# print(worst_student.name, worst_student.surname)
# print(worst_student.grades)

# print(some_lect.name, some_lect.surname)
# print(some_lect.grades)


print(some_reviewer)
print(some_lecturer)
print(some_student)

#
rate_people(some_student, worst_student)
rate_people(some_lecturer, else_lecturer)

students_list = []
students_list.append(some_student.av_grade())
students_list.append(worst_student.av_grade())

lecturers_list = []
lecturers_list.append(some_lecturer.av_grade())
lecturers_list.append(else_lecturer.av_grade())

def avg_grades(list, course):
    sum_grades = 0    
    for grade in list:
        sum_grades += grade
    return sum_grades / len(students_list), course

average_grades_for_students = avg_grades(students_list, 'Python')
print(f'Средняя оценка студентов: {average_grades_for_students}')
average_grades_for_lecturers = avg_grades(lecturers_list, 'Python')
print(f'Средняя оценка лекторов: {average_grades_for_lecturers}')