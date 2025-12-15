
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
        s.list()


def show_student_marks(cid, marks_data):
    print(f"\n--- Marks for course {cid} ---")

    if not marks_data:
        print("No courses available.")
        return

    for student, score in marks_data:
        if score == -1:
            print(f"Student ({student.get_id()}) - {student.get_name()}: Not graded")
        else:
            print(f"Student ({student.get_id()}) - {student.get_name()}: {score}")
