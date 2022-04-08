import math
import numpy as np
import curses

class Student:
    def __init__(self, name, id, dob, mark, gpa, credit):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__mark = mark
        self.__gpa = gpa
        self.__credit = credit

    def getname(self):
        return self.__name

    def getid(self):
        return self.__id

    def getdob(self):
        return self.__dob
    
    def getmark(self):
        return self.__mark

    def getgpa(self):
        return self.__gpa

    def getcredit(self):
        return self.__credit

    def setname(self, name):
        self.__name = name

    def setid(self, id):
        self.__id = id

    def setdob(self, dob):
        self.__dob = dob

    def setmark(self, mark):
        self.__mark = mark

    def setgpa(self, gpa):
        self.__gpa = gpa

    def setcredit(self, credit):
        self.__credit = credit

    def input():
        name = str(input("Enter student name: "))
        id = str(input("Enter student id: "))
        dob = str(input("Enter student date of birth: "))
        mark = []
        gpa = []
        credit = []
        student = {
            "studentname" : name,
            "studentid" : id,
            "studentdob" : dob,
            "studentmark" : mark,
            "studentgpa" : gpa,
            "credit" : credit
        }
        return student

class Course:
    def __init__(self, name, id) -> None:
        self.__name = name
        self.__id == id

    def getname(self):
        return self.__name

    def getid(self):
        return self.__id

    def setname(self, name):
        self.__name = name

    def setid(self, id):
        self.__id = id

    def input():
        name = str(input("Enter course name: "))
        id = str(input("Enter course ID: "))
        course = {
            "coursename" : name,
            "courseid" : id
        }
        return course

## get number of students
def getNoStudents():
    students_no = int(input("Enter number of students: "))
    return students_no

## get student info
def getStudentInfo(students_no):
    students = []
    for i in range(0, students_no):  
        students.append(Student.input())
    return students

## get number of courses
def getNoCourses():
    courses_no = int(input("Enter number of courses: "))
    return courses_no

## get course info
def getCourseInfo(courses_no):
    courses = []
    for i in range(0, courses_no):  
        courses.append(Course.input())
    return courses

## show students
def showStudents(students):
    print("All students: ")
    for student in students:
        print(f"Name: {student['studentname']: <20} ID: {student['studentid']: <10} Date of Birth: {student['studentdob']: <15}")

## show courses
def showCourses(courses):
    print("All students: ")
    for course in courses:
        print(f"Name: {course['coursename']: <20} ID: {course['courseid']: <10}")

## get marks
def getMark(courses, students):
    courseid = str(input("Enter course id: "))
    for i in range(len(courses)):
        if courseid == courses[i]["courseid"]:
            print("Course selected: " + courses[i]['coursename'])
            for j in range(len(students)):
                students[j]["studentmark"] = float(input("Enter mark of student " + students[j]["studentname"] + ": "))
                students[j]["credit"] = int(input("Enter credit of student " + students[j]["studentname"] + ": "))
                students[j]["studentmark"] = math.floor(students[j]["studentmark"])
                students[j]['studentgpa'] = np.dot(students[j]['studentmark'], students[j]['credit'])

## show marks
def showMark(courses, students):
    courseid = str(input("Enter course ID: "))
    for i in range (len(courses)):
        if courseid == courses[i]['courseid']:
            print("Course selected: " + courses[i]['coursename'])
            for j in range (len(students)):
                print(f"Student: {students[j]['studentname']: <20} Mark: {students[j]['studentmark']: <10} Credit: {students[j]['credit']: < 10} GPA: {students[j]['studentgpa']}")

## continue process
def continueprocess():
    runagain = input("Continue? (yes/no): ")
    if (runagain.lower() == "yes"):
        interface()
    elif (runagain.lower() == "no"):
        quit("Goodbye...")
    else:
        print("Invalid choice!")
        continueprocess()

## UI
def interface():
    print("1. Show list of students")
    print("2. Show list of courses")
    print("3. Add marks to course")
    print("4. Show marks of course")
    print("5. Exit")

    try:
        x = int(input("Enter a choice: "))
    except ValueError:
        exit("Invalid choice!")
    if (x == 1):
        showStudents(students)
        continueprocess()
    elif (x == 2):
        showCourses(courses)
        continueprocess()
    elif (x == 3):
        getMark(courses, students)
        continueprocess()
    elif (x == 4):
        showMark(courses, students)
        continueprocess()
    elif (x == 5):
        quit("Goodbye...")

if __name__ == "__main__":
    students_no = getNoStudents()
    students = getStudentInfo(students_no)

    courses_no = getNoCourses()
    courses = getCourseInfo(courses_no)

    interface()

    






