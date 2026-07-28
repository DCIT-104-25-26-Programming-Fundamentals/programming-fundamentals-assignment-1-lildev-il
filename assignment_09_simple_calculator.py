# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#

# Function to add a student
def add_student(students):
    name = input("Student name: ")
    student_id = input("Student ID: ")

    num_scores = int(input("How many scores? "))
    scores = []

    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)
    print(f'Student "{name}" added successfully.')


# Function to display all students
def display_students(students):
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n---------------------------------------------------------------")
    print("Name\t\tID\t\tScores\t\tAverage")
    print("---------------------------------------------------------------")

    for student in students:
        total = 0
        for score in student["scores"]:
            total += score

        average = round(total / len(student["scores"]), 2)

        score_list = ""
        for i in range(len(student["scores"])):
            score_list += str(student["scores"][i])
            if i < len(student["scores"]) - 1:
                score_list += ", "

        print(f"{student['name']}\t{student['id']}\t{score_list}\t{average}")

    print("---------------------------------------------------------------")


# Function to calculate the average score of one student
def calculate_average(students):
    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            total = 0
            for score in student["scores"]:
                total += score

            average = round(total / len(student["scores"]), 2)

            print(f"{student['name']}'s average score: {average}")
            return

    print("Error: Student ID not found.")


# Main Program
students = []

while True:
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        calculate_average(students)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Error: Invalid choice. Please enter a number from 1 to 4.")

