#simple project employee databas system 
#features  add employee , viwe employee , search employee,delete employee, exit
#concepts used  variables , input/output, list, dictionay, function , loop, conditions 


print("="*40)
print("\t EMPLOYEE DATABASE SYSTEM")
print("="*40)

#menu 
# while True:
#     print("\n 1. ADD EMPLOYEE")
#     print(" 2. VIWE EMPLOYEES")
#     print(" 3. SEARCH EMPLOYEE")
#     print(" 4. DELETE EMPLOYEE")
#     print(" 5. EXIT")
#     break


# list for storing employee details
employees = []


# fuction for adding employeee
def add_employee():

    #take details from user
    print("-"*30)
    print(" Employee Information")
    print("-"*30)
    name = input(         "Name :")
    age = int(input(      "Age  :"))
    employe_ID =int(input("ID   :"))
    role = input(         "Role :")
    experience=int(input("Experience (YEARS):"))

#dictionary for the employee details 
    employee = {
        "name": name,
        "age": age,
        "id": employe_ID,
        "role": role,
        "experience": experience
    }
# add employee to list 
    employees.append(employee)
    print("Employee added successfully!")

# function for vewi employee from the list
def view_employees():
    #for checking if there is no employee in the list
    if len(employees) == 0:
        print("No employees found.")
    else:
         print("-"*30)
         print(" Employee Information")
         print("-"*30)
     
     #check each employee one by one in list of employess
         for employee in employees:
            print("Name:", employee["name"])
            print("Age:", employee["age"])
            print("ID:", employee["id"])
            print("Role:", employee["role"])
            print("Experience:", employee["experience"])
            print("-"*30)


# fuction for search employee in a list
def search_employee():
    search_ID = int(input("Enter Employee ID for search :"))
    for employee in employees:
            if  employee["id"] ==   search_ID:
             print("Name:", employee["name"])
             print("Age:", employee["age"])
             print("ID:", employee["id"])
             print("Role:", employee["role"])
             print("Experience:", employee["experience"])
             print("Employee Found")
             print("~"*30)
             break
    else:
        print("Sorry Employee Not Found ")

     
     #function for delete employee in the list
def delete_employee():
    delete_ID = int(input("Enter Employee ID for delete :"))
    for employee in employees:
            if employee["id"] == delete_ID:
             employees.remove(employee)
             print("Name:", employee["name"])
             print("Age:", employee["age"])
             print("ID:", employee["id"])
             print("Role:", employee["role"])
             print("Experience:", employee["experience"])
             print("Employee deleted from the RECORDS successfully")
             print("="*30)
             break
    else:
        print(" Employee of this ID is  Not Found ")
while True:

    print("\n 1. ADD EMPLOYEE")
    print(" 2. VIWE EMPLOYEES")
    print(" 3. SEARCH EMPLOYEE")
    print(" 4. DELETE EMPLOYEE")
    print(" 5. EXIT")
    

   #choose from the menu
    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice =="4":
        delete_employee()
    elif choice=="5":
        print("Exiting Program....")
        break
    else:
         print("Invalid choice.")
