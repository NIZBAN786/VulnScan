import modules.db as db

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
        print(f"Welcome {name}!")
    else:
        print("Login failed")
