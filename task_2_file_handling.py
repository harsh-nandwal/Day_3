import json 

Employees = []

def save_data():
    with open("employees.json", 'w') as file:
        json.dump(Employees, file, indent=4)
    
    print("Student data saved successfully.")


def load_data():
    global Employees

    try:
        with open("employees.json", "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                print("Data loaded successfully.")
                Employees = data
            else:
                Employees = []
                print("Invalid employee data format.")

    except FileNotFoundError:
        Employees = []
        print("No previous data found. Starting with an empty record.")

    except json.JSONDecodeError:
        Employees = []
        print("The JSON file is empty or invalid. Starting with an empty record.")


def add_employees_details():
    try:
        employee_id = int(input("Enter your id : "))

        if employee_id <= 0:
            print("Employee ID must be greater than zero.")
            return

        for emp in Employees:
            if emp["employee_id"] == employee_id:
                print("Employee ID already exists.")
                return  

        name = input("Enter your name : ")
        email = input("Enter your email : ")
        department = input("Enter your department : ")
        salary = int(input("Enter your salary : "))

        if not employee_id or not name or not email or not department or not salary:
            print("Error: All fields are required.")
            return

        if salary <= 0:
            print("Error: Salary must be greater than zero.")
            return 

        if '@' not in email or '.' not in email:
            print("Error: Invalid email address.")
            return 


        employee = {
            "employee_id": employee_id, 
            "name": name, 
            "email": email, 
            "department": department, 
            "salary": salary
        }

        Employees.append(employee)
        save_data()
        print("Data added successfully")

    except ValueError:
        print("Please enter valid numeric values for ID and salary.") 


def display_employee():
    if not Employees:
        print("No employee records found.")
        return

    
    print("\n------ Employee Details ------")

    for emp in Employees:
        print("-----------------------------")
        print(emp)


def search_employee():
    try:
        employee_id = int(input("Enter employee id :"))

        for emp in Employees:
            if emp["employee_id"] == employee_id:
                print("Employee Found")
                print(emp)
                return 

        print("Employee ID not found")

    except ValueError:
        print("Please enter a valid Employee ID.")


def update_employee():
    try:
        employee_id = int(input("Enter Employee ID: "))

        for emp in Employees:
            if emp["employee_id"] == employee_id:

                print("Employee Found!")
                print(emp)

                print("What do you want to update?")
                print("1. Department")
                print("2. Salary")

                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    department = input("Enter new department: ").strip()

                    if not department:
                        print("Department cannot be empty.")
                        return

                    emp["department"] = department

                elif choice == "2":
                    try:
                        salary = float(input("Enter new salary: "))

                        if salary <= 0:
                            print("Salary must be greater than zero.")
                            return

                        emp["salary"] = salary

                    except ValueError:
                        print("Please enter a valid salary.")
                        return

                else:
                    print("Invalid choice.")
                    return

                save_data()
                print("Employee details updated successfully.")
                return

        print("Employee ID not found.")

    except ValueError:
        print("Please enter a valid Employee ID.")


def delete_employee():
    try:
        employee_id = int(input("Enter Employee ID : ").strip())

        for emp in Employees:
            if emp["employee_id"] == employee_id:
                Employees.remove(emp)
                save_data()
                print("Data deleted successfully.")
                return 
            
        print("Error: Employee not found.")

    except ValueError:
        print("Please enter a valid Employee ID.")


def total_employees():
    print(len(Employees))


load_data()

while True:
    print("1. Add employee details")
    print("2. Save employee details")
    print("3. View employee details")
    print("4. Search employee")
    print("5. Update employee details")
    print("6. Delete employee")
    print("7. Total number of employees")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        add_employees_details()
    elif choice == 2:
        save_data()
    elif choice == 3:
        display_employee()
    elif choice == 4:
        search_employee()
    elif choice == 5:
        update_employee()
    elif choice == 6:
        delete_employee()
    elif choice == 7:
        total_employees()
    else:
        print("Invalid Choice. Please select 1-7.")

