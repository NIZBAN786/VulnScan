import modules.db as db
import modules.welcome as welcome
import pyfiglet
import modules.virustotal as virustotal
def register():
    user_document = {
        "name": input("Enter your name: "),
        "email": input("Enter your email: "),
        "password": input("Enter your password: "),
        "phone": input("Enter your phone: ")
    }
    db.collection.insert_one(user_document)

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")  
    user = db.collection.find_one({"email": email})
    if user and user["password"] == password:
        name = user.get('name')
        r = pyfiglet.figlet_format(f"Welcome {name}!", font = "slant")
        print(r)       
        while True:
            print("1. Scan URL with VirusTotal")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                result = virustotal.phish_checker()
                print(result)
            elif choice == "2":
                break
            else:
                print("Invalid choice")
        
    else:
        print("Login failed")
