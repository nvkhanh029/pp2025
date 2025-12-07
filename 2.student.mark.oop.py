class Entity:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Student(Entity):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.__dob = dob

    def get_dob(self):
        return self.__dob

    def list(self):
        print(f"ID: {self.get_id()}   | Name: {self.get_name()}   | DoB: {self.__dob}")


class Course(Entity):
    def list(self):
        print(f"ID: {self.get_id()}   | Name: {self.get_name()}")


class Mark:
    def __init__(self, cid, sid, mark):
        self.__cid = cid
        self.__sid = sid
        self.__mark = mark

    def get_course_id(self):
        return self.__cid

    def get_student_id(self):
        return self.__sid

    def get_mark(self):
        return self.__mark


class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []


    def input_students(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            print(f"\n--- Student {i+1} ---")
            sid = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Date of birth: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input("\nEnter number of courses: "))
        for i in range(n):
            print(f"\n--- Course {i+1} ---")
            cid = input("Course ID: ")
            name = input("Course name: ")
            self.courses.append(Course(cid, name))

    def input_marks(self):
        cid = input("Enter course: ")

        found_course = False
        for c in self.courses:
            if c.get_id() == cid:
                found_course = True
                break
        
        if found_course == False:
            print("Course not found!")
            return

        print("\nEnter marks:")
        for s in self.students:
            val = float(input(f"Mark for {s.get_name()} ({s.get_id()}): "))
            self.marks.append(Mark(cid, s.get_id(), val))


    def list_courses(self):
        print("\n--- Course list ---")
        for c in self.courses:
            c.list()

    def list_students(self):
        print("\n--- Student list ---")
        for s in self.students:
            s.list()

    def show_student_marks(self):
        if not self.courses:
            print("No courses available.")
            return

        cid = input("\nEnter Course ID to view marks: ")

        print(f"\n--- Marks for course {cid} ---")
        
        found_marks = False
        for s in self.students:
            student_mark = None
            for m in self.marks:
                if m.get_course_id() == cid and m.get_student_id() == s.get_id():
                    student_mark = m.get_mark()
                    break
            
            if student_mark is not None:
                print(f"Student {s.get_name()} ({s.get_id()}): {student_mark}")
                found_marks = True
            else:
                print(f"Student {s.get_name()} ({s.get_id()}): Not graded")


m = Management()

while True:
    print("\n====== Student Mark Management ======")
    print("1. Input students")
    print("2. Input courses")
    print("3. Enter marks for a course")
    print("4. List courses")
    print("5. List students")
    print("6. Show student marks for a course")
    print("0. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        m.input_students()
    elif choice == "2":
        m.input_courses()
    elif choice == "3":
        m.input_marks()
    elif choice == "4":
        m.list_courses()
    elif choice == "5":
        m.list_students()
    elif choice == "6":
        m.show_student_marks()
    elif choice == "0":
        print("Bye!")
        break
    else:
        print("Invalid choice, please try again.")