from .entity import Entity

class Student(Entity):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.__dob = dob
        self.__gpa = 0.0

    def get_dob(self):
        return self.__dob

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def list(self):
        print(f"ID: {self.get_id()}   | Name: {self.get_name()}   | DoB: {self.get_dob()}   | GPA: {self.get_gpa()}")
