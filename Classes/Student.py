from Person import Person


class Student(Person):
    def __init__(self, given_name, middle_name, last_name, degree):
        super().__init__(given_name, middle_name, last_name)
        self.__degree = degree

    def student_info(self):
        return f"{self.personal_info()}\nDegree: {self.__degree}"
