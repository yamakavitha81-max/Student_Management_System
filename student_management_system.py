import json
try:
    with open("students.json","r")as file:
        students=json.load(file)
except:
    students=[]
def save_data():
    with open("students.json","w")as file:
        json.dump(students,file,indent=4)
def add_student():
    print("====ADD STUDENT====")
    student_id=input("enter id number:")
    #check duplicate id
    for student in students:
        if student["ID"]==student_id:
            print("Student ID already exist!")
            return
    name=input("enter name:")
    #validate age
    while True:
        age=input("Enter age:")
        if age.isdigit() and int(age)>0:
            break
        print("Invalid age!Enter a Positive Number")
    course=input("enter course:")
    #validate marks
    while True:
        marks=input("enter marks:")
        if marks.isdigit() and 0<=int(marks)<=100:
            break
        print("Marks should between 0 and 100.")

    student={
        "ID":student_id,
        "Name":name,
        "Age":age,
        "Course":course,
        "Marks":marks
    }
    students.append(student)
    save_data()
    print("student added successfully!\n")
def view_students():
    print("----student list----")
    if len(students)==0:
        print("No Student Found.\n")
        return
    for student in students:
        print("---------------------------------")
        print("ID:",student["ID"])
        print("Name:",student["Name"])
        print("Age:",student["Age"])
        print("Course:",student["Course"])
        print("Marks:",student["Marks"])
    print("--------------------------------------\n")
def search_student():
    print("\n ------search student-----")
    student_id=input("Enter Student ID:")
    for student in students:
        if student["ID"]==student_id:
            print("student found!")
            print("ID:",student["ID"])
            print("Name:",student["Name"])
            print("Age:",student["Age"])
            print("Course:",student["Course"])
            print("Marks:",student["Marks"])

            return
    print("student not found!")
def update_student():
    print("\n------------Update student-------------")
    student_id = input("Enter Student ID:")

    for student in students:
        if student["ID"] == student_id:
            print("Student Found!")

            student["Name"] = input("Enter New Name:")

            while True:
                age = input("Enter New Age: ")
                if age.isdigit() and int(age) > 0:
                    student["Age"] = age
                    break
                print("Invalid Age!")

            student["Course"] = input("Enter New Course:")

            while True:
                marks = input("Enter New Marks: ")
                if marks.isdigit() and 0 <= int(marks) <= 100:
                    student["Marks"] = marks
                    break
                print("Marks should be between 0 and 100.")

            save_data()
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")
def delete_student():
    print("\n----delete student----")
    student_id=input("enter student id:")
    for student in students:
        if student["ID"]==student_id:
            students.remove(student)
            save_data()
            print("student deleted successfully!")
            return 
    print("student not found")
def student_statistics():
    if len(students)==0:
        print("\nNo students available!.")
        return
    total=len(students)
    marks=[]
    for student in students:
        marks.append(int(student["Marks"]))
    heighest=max(marks)
    lowest=min(marks)
    average=sum(marks)/total
    print("------Student Statistics------")
    print("Toatl Students:",total)
    print("Heighest Marks:",heighest)
    print("Lowest Marks:",lowest)
    print("Average Marks:",round(average,2))
def sort_students():
    if len(students)==0:
        print("\nNo students available!")
        return
    print("\n Sort by")
    print("1.Name")
    print("2.Marks")
    choice=input("Enter choice:")
    if choice=="1":
        students.sort(key=lambda student:student["Name"])
        save_data()
        print("Students Sort by Name.")
    elif choice=="2":
        students.sort(key=lambda student:int(student["Marks"]) ,reverse=True)
        save_data()
        print("Students sort by marks")
    else:
        print("Invalid choice.")
def topper_student():
    if len(students)==0:
        print("No stduents avialable!")
        return 
    topper=max(students,key=lambda student:int(student["Marks"]))
    print("-----Topper Student-----")
    print("ID:",topper["ID"])
    print("Name:",topper["Name"])
    print("course:",topper["Course"])
    print("Marks:",topper["Marks"])

    
while True:
    print("==============STUDENT MANAGEMENT SYSTEM=================")
    print("1.add student")
    print("2.view students")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.student statistics")
    print("7.sort students")
    print("8.topper_student")
    print("9.exit")
    choice =input("enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        update_student()
    elif choice=="5":
        delete_student()
    elif choice=="6":
        student_statistics()
    elif choice=="7":
        sort_students()
    elif choice=="8":
        topper_student()
    elif choice=="9":
        print("Thank youuu!")
        break

    else:
        print("invalid choice!")
    