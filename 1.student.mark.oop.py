# 1.student.mark.py

students = []        # list of dicts: { "id": ..., "name": ..., "dob": ... }
courses = []         # list of dicts: { "id": ..., "name": ... }
marks = {}           # dict: { course_id: { student_id: mark } }


def input_num_students():
    n = int(input("Enter number of students in the class: "))
    return n


def input_student_info(num_students):
    for i in range(num_students):
        print(f"\nStudent {i+1}:")
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("Date of birth (dd/mm/yyyy): ")
        student = {"id": sid, "name": name, "dob": dob}
        students.append(student)


def input_num_courses():
    n = int(input("Enter number of courses: "))
    return n


def input_course_info(num_courses):
    for i in range(num_courses):
        print(f"\nCourse {i+1}:")
        cid = input("ID: ")
        name = input("Name: ")
        course = {"id": cid, "name": name}
        courses.append(course)


def select_course():
    if not courses:
        print("No courses available.")
        return None

    print("\nAvailable courses:")
    for i, c in enumerate(courses):
        print(f"  {i+1}. {c['id']} - {c['name']}")
    idx = int(input("Select a course by number: ")) - 1

    if 0 <= idx < len(courses):
        return courses[idx]["id"]
    else:
        print("Invalid selection.")
        return None


def input_marks(course_id):
    if not students:
        print("No students available.")
        return

    if course_id not in marks:
        marks[course_id] = {}

    print(f"\nEntering marks for course {course_id}:")
    for s in students:
        while True:
            try:
                m = float(input(f"Mark for student {s['id']} - {s['name']}: "))
                break
            except ValueError:
                print("Invalid mark. Please enter a number.")
        marks[course_id][s["id"]] = m



def list_courses():
    print("\n--- Course list ---")
    if not courses:
        print("No courses.")
        return

    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")


def list_students():
    print("\n--- Student list ---")
    if not students:
        print("No students.")
        return

    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")


def show_student_marks():
    if not courses:
        print("No courses available.")
        return

    cid = select_course()
    if cid is None:
        return

    print(f"\n--- Marks for course {cid} ---")
    if cid not in marks or not marks[cid]:
        print("No marks entered for this course yet.")
        return

    for s in students:
        sid = s["id"]
        if sid in marks[cid  ]:
            print(f"Student {sid} - {s['name']}: {marks[cid][sid]}")
        else:
            print(f"Student {sid} - {s['name']}: no mark")



def main():
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
            n = input_num_students()
            input_student_info(n)
        elif choice == "2":
            n = input_num_courses()
            input_course_info(n)
        elif choice == "3":
            cid = select_course()
            if cid is not None:
                input_marks(cid)
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
