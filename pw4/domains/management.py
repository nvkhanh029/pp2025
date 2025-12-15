import math
import numpy as np


class Mana:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks_arr = None


    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)


    def get_course_index(self, cid):
        for i, c in enumerate(self.courses):
            if c.get_id() == cid:
                return i
        return -1
    
    def init_mark_arr(self):
        if self.marks_arr is None:
            rows = len(self.students)
            cols = len(self.courses)
            self.marks_arr = np.full((rows, cols), -1.0)        # Create a matrix of size (students x courses) filled with -1.0

    def set_marks(self, col_idx, row_idx, val):
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


    def get_student_marks(self, col_idx):
        if self.marks_arr is None:
            print("No courses available.")
            return

        marks_list = []
        for row_idx, s in enumerate(self.students):
            score = self.marks_arr[row_idx][col_idx]
            marks_list.append((s, score))
        return marks_list
    
