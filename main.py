import modules.welcome as welcome
import modules.db as db
import modules.register as register
import modules.virustotal as virustotal

welcome.welcome()
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register.register()
    elif choice == "2":
        register.login()
    elif choice == "3":
        break
    else:
        print("Invalid choice")