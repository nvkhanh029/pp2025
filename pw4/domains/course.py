from .entity import Entity

class Course(Entity):
    def __init__(self, id, name, cre):
        super().__init__(id, name)
        self.__cre = cre

    def get_credits(self):
        return self.__cre
    
    def list(self):
        print(f"ID: {self.get_id()}   | Name: {self.get_name()}   | Credits: {self.get_credits()}")
