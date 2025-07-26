# FILE_NAME = "employees.txt"

def load_data():
    try:
        with open("emp.txt", "r") as file:
            return [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_data(data):
    with open("emp.txt", "w") as file:
        for emp in data:
            file.write(",".join(emp) + "\n")

def insert_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    dept_no = input("Enter Department Number: ")
    data = load_data()
    data.append([emp_id, name, email, dept_no])
    save_data(data)
    print("Employee added successfully!\n")

def update_email():
    emp_id = input("Enter Employee ID to update email: ")
    data = load_data()
    updated = False
    for emp in data:
        if emp[0] == emp_id:
            emp[2] = input("Enter new Email: ")
            updated = True
            break
    if updated:
        save_data(data)
        print("Email updated successfully!\n")
    else:
        print("Employee not found!\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    data = load_data()
    new_data = [emp for emp in data if emp[0] != emp_id]
    if len(new_data) < len(data):
        save_data(new_data)
        print("Employee deleted successfully!\n")
    else:
        print("Employee not found!\n")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    data = load_data()
    for emp in data:
        if emp[0] == emp_id:
            print("Employee Found:", emp)
            return
    print("Employee not found!\n")

def search_by_dept():
    dept_no = input("Enter Department Number: ")
    data = load_data()
    found = [emp for emp in data if emp[3] == dept_no]
    if found:
        for emp in found:
            print(emp)
    else:
        print("No employees found in this department!\n")

def show_all():
    data = load_data()
    if data:
        for emp in data:
            print(emp)
    else:
        print("No employees found!\n")

def main():
    while True:
        print("""
        Welcome to EMS
        Main Menu
        1) Insert new employee
        2) Update email ID of employee
        3) Delete employee by ID
        4) Search employee
        5) Search according to department number
        6) Show all employees
        7) Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            insert_employee()
        elif choice == "2":
            update_email()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            search_by_dept()
        elif choice == "6":
            show_all()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "_main_":
    main()


