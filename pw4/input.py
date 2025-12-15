from domains.student import Student 
from domains.course import Course


def input_students(m):
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        sid = input("Student ID: ")
        name = input("Student name: ")
        dob = input("Date of birth: ")
        m.students.append(Student(sid, name, dob))


def input_courses(m):
    n = int(input("\nEnter number of courses: "))

    for i in range(n):
        print(f"\n--- Course {i+1} ---")
        cid = input("Course ID: ")
        name = input("Course name: ")
        cre = int(input("Course credits: "))
        m.courses.append(Course(cid, name, cre))


def input_marks(m):
    if not m.courses or not m.students:
        print("Please input students and courses first.")
        return

    m.init_mark_arr()

    cid = input("\nEnter Course ID to input marks: ")
    col_idx = m.get_course_index(cid)
    
    if col_idx == -1:
        print("Course not found!")
        return

    print(f"Enter marks for course {cid}:")

    for row_idx, s in enumerate(m.students):
        val = float(input(f"Mark for student {s.get_id()} - {s.get_name()}: "))
        if 0 <= val <= 20:
            m.set_marks(col_idx, row_idx, val)
        else:
            print("Invalid mark!")
