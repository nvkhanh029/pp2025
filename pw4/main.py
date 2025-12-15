from domains.management import Mana
from input import *
from output import *


def main():
    m = Mana()

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
            input_students(m)
        elif choice == "2":
            input_courses(m)
        elif choice == "3":
            input_marks(m)
        elif choice == "4":
            list_courses(m.courses)
        elif choice == "5":
            list_students(m.students)

        elif choice == "6":
            if not m.courses:
                print("Please input courses first.")
                continue
                
            cid = input("\nEnter Course ID to view marks: ")
            col_idx = m.get_course_index(cid)

            if col_idx == -1:
                print("Course not found!")
                continue

            marks_data = m.get_student_marks(col_idx)
            show_student_marks(cid, marks_data)
        
        elif choice == "7":
            m.sortby_gpa()
            print("\n--- Student List Sorted by GPA (Descending) ---")
            list_students(m.students)
                
        elif choice == "0":
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
