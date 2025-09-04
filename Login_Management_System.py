import getpass 
Login_data = {}

while True:
    choice = int(input("Enter 1 --> Register , 2 --> Login, 3 --> Quit: "))

    if choice == 1:  # Register
        username = input("Enter your Username: ")
        passw = input("Enter your Password: ")

        if username in Login_data:
            print("Username already exists! Choose another.")
        else:
            Login_data[username] = {"password": passw, "attempts": 0, "locked": False}
            print("Registration successful!")

    elif choice == 2:  # Login
        username = input("Enter your Username: ")

        if username not in Login_data:
            print("Username not found. Please register first.")
            continue

        # If account locked
        if Login_data[username]["locked"]:
            print("Account is locked due to too many failed attempts.")
            continue

        passw = input("Enter your Password: ")

        if Login_data[username]["password"] == passw:
            print("Login successful!")
            Login_data[username]["attempts"] = 0  # reset after success
        else:
            Login_data[username]["attempts"] += 1
            print("Invalid password.")

            if Login_data[username]["attempts"] >= 3:
                Login_data[username]["locked"] = True
                print("Too many failed attempts. Account locked!")

    elif choice == 3:  # Quit
        print("Exiting The Program!")
        break

    else:
        print("Invalid choice, try again.")