#small project on Students record system
#concepts used functions , lists, dictionaries and loop 
#faetures 
#add students , show students ,


print("="*40)
print("STUDENT RECORD MANAGEMENT SYSTEM")
print("="*40)

students = []


# function for adding students 
def add_student():


#take input from user 
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    department = input("Enter Department: ")

#create dictionary for students info
    student = {
        "Name": name,
        "RollNo": roll_no,
        "Department": department
    }

# added to the list through this 
    students.append(student)

    print("Student Added Successfully!\n")


# function for show students in a list 
def show_students():



# check if lenght of list if there is no students in the list 
    if len(students) == 0:
        print("No Student Records Found")
        return

#here with in keyword we check things inside the dictionaries
    for student in students:
        
        print("Name      :", student["Name"])
        print("Roll No   :", student["RollNo"])
        print("Department:", student["Department"])


while True:
  print("1. Add Student")
  print("2. Show Students")

  choice = input("Enter Your Choice: ")
  if choice == "1":
   add_student()

  elif choice == "2":
   show_students()

  else:
     print("Invalid Choice")