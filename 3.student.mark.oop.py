import math
import numpy as np

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
        self.__gpa = 0.0

    def get_dob(self):
        return self.__dob

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def list(self):
        print(f"ID: {self.get_id()}   | Name: {self.get_name()}   | DoB: {self.get_dob()}   | GPA: {self.get_gpa()}")


class Course(Entity):
    def __init__(self, id, name, cre):
        super().__init__(id, name)
        self.__cre = cre

    def get_credits(self):
        return self.__cre
    
    def list(self):
        print(f"ID: {self.get_id()}   | Name: {self.get_name()}   | Credits: {self.get_credits()}")

class Management:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks_arr = None


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
            cre = int(input("Course credits: "))
            self.courses.append(Course(cid, name, cre))


    def init_arr(self):
        if self.marks_arr is None:
            rows = len(self.students)
            cols = len(self.courses)
            self.marks_arr = np.full((rows, cols), -1.0)        # Create a matrix of size (students x courses) filled with -1.0


    def input_marks(self):
        if not self.courses or not self.students:
            print("Please input students and courses first.")
            return
        
        self.init_arr()

        cid = input("\nEnter Course ID to input marks: ")

        col_idx = -1
        for i, c in enumerate(self.courses):
            if c.get_id() == cid:
                col_idx = i
                break
        
        if col_idx == -1:
            print("Course not found!")
            return
        
        print(f"Enter marks for course {cid}:")

        for row_idx, s in enumerate(self.students):
                val = float(input(f"Mark for student {s.get_id()} - {s.get_name()}: "))
                score = math.floor(val * 10) / 10
                self.marks_arr[row_idx][col_idx] = score


    def calculate_gpa(self):
        if self.marks_arr is None:
            print("No marks data.")
            return
        
        credits = np.array([c.get_credits() for c in self.courses])
        for i, student in enumerate(self.students):
            student_marks = self.marks_arr[i]

            mask = student_marks != -1          # Filter out -1

            if np.any(mask):
                valid_marks = student_marks[mask]
                valid_credits = credits[mask]

                total_weighted_score = np.sum(valid_marks * valid_credits)
                total_credits = np.sum(valid_credits)

                if total_credits > 0:
                    gpa = total_weighted_score / total_credits
                    student.set_gpa(gpa)
            else:
                student.set_gpa(0.0)


    def sortby_gpa(self):
        self.calculate_gpa()
        self.students.sort(key=lambda x: x.get_gpa(), reverse=True)
        
        # key=lambda x: x.get_gpa() tells Python to look at the GPA of the object
        # reverse=True makes it Descending (High -> Low)
        
        print("\n--- Student List Sorted by GPA (Descending) ---")
        for s in self.students:
            s.list()


    def list_courses(courses):
        print("\n--- Course list ---")
        if not courses:
            print("No courses available.")
            return
        for c in courses:
            c.list()

    def list_students(students):
        print("\n--- Student list ---")
        if not students:
            print("No students available.")
            return
        for s in students:
            print(s.list())


    def show_student_marks(self):
        if self.marks_arr is None:
            print("No courses available.")
            return

        cid = input("\nEnter Course ID to view marks: ")

        print(f"\n--- Marks for course {cid} ---")
        
        col_idx = -1
        for i, c in enumerate(self.courses):
            if c.get_id() == cid:
                col_idx = i
                break

        if col_idx == -1:
            return
        
        for row_idx, s in enumerate(self.students):
            score = self.marks_arr[row_idx][col_idx]

            if score == -1:
                print(f"Student ({s.get_id()}) - {s.get_name()}: Not graded")
            else:
                print(f"Student ({s.get_id()}) - {s.get_name()}: {score}")



m = Management()

while True:
    print("\n====== Student Mark Management ======")
    print("1. Input students")
    print("2. Input courses")
    print("3. Enter marks for a course")
    print("4. List courses")
    print("5. List students")
    print("6. Show student marks for a course")
    print("7. Calculate & Sort students by GPA")
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
    elif choice == "7":
        m.sortby_gpa()
    elif choice == "0":
        print("Exiting.")
        break
    else:
        print("Invalid choice, please try again.")
