import streamlit as st

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class SchoolManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        student = Student(name, roll_number, grade)
        self.students.append(student)
        st.success("Student added successfully!")

    def view_students(self):
        if not self.students:
            st.info("No students found.")
        else:
            for student in self.students:
                st.write(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")

    def remove_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                st.success("Student removed successfully!")
                return
        st.warning("Student not found.")

# Creating an instance of the SchoolManagementSystem
school = SchoolManagementSystem()

# Streamlit app
def main():
    st.title("School Management System")

    menu = ["Add Student", "View Students", "Remove Student"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Student":
        name = st.text_input("Enter student name")
        roll_number = st.text_input("Enter student roll number")
        grade = st.text_input("Enter student grade")
        if st.button("Add"):
            school.add_student(name, roll_number, grade)

    elif choice == "View Students":
        school.view_students()

    elif choice == "Remove Student":
        roll_number = st.text_input("Enter student roll number to remove")
        if st.button("Remove"):
            school.remove_student(roll_number)

if __name__ == '__main__':
    main()
