contacts = []

while True:
    choice = input("""
    1 : Display All Students
    2 : Add Student
    3 : Delete Student
    4 : Search Student
    5 : Exit
    
Choose: """)

    if choice == "1":
        if len(contacts) == 0:
            print("No students yet.")
        else:
            for student in contacts:
                print("----------------")
                print("Name :", student["name"])
                print("Number :", student["number"])

    elif choice == "2":
        number = input("Enter student number: ")

        if not number.isdigit():
            print("Number must contain digits only.")
            continue

        number = int(number)

        found = False
        for student in contacts:
            if student["number"] == number:
                found = True
                break

        if found:
            print("This number already exists.")
        else:
            name = input("Enter student name: ")
            contacts.append({
                "name": name,
                "number": number
            })
            print("Student added successfully.")

    elif choice == "3":
        delete_code = input("Enter student name or number: ")

        found = False

        for student in contacts:
            if student["name"] == delete_code or str(student["number"]) == delete_code:
                contacts.remove(student)
                print("Student deleted.")
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        search = input("Enter student name or number: ")

        found = False

        for student in contacts:
            if student["name"] == search or str(student["number"]) == search:
                print("Name :", student["name"])
                print("Number :", student["number"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        print("Goodbye ^_^ ")
        break

    else:
        print("Invalid choice.")
