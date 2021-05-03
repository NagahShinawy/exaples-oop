"""
created by Nagaj at 03/05/2021
"""


class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class LearnerMixin(Person):
    def __init__(self, *args, **kwargs):
        super(LearnerMixin, self).__init__(*args, **kwargs)
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class TeacherMixin(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Tutor(LearnerMixin, TeacherMixin):
    def __init__(self, *args, **kwargs):
        super(Tutor, self).__init__(*args, **kwargs)


jane = Tutor("Jane", "Smith", "SMTJNX045")
jane.enrol("a_postgrad_course")
jane.assign_teaching("an_undergrad_course")
