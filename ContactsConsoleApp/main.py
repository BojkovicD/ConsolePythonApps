#MAIN MENU
def application():
    print("|-------------------|")
    print("|1. Add new contact |")
    print("|2. See all contacts|")
    print("|3. Delete contact  |")
    print("|4. Exit            |")
    print("|-------------------|")
    option = input()
    if option == "1":
        AddContact()
    elif option == "2":
        SeeContacts()
    elif option == "3":
        DeleteContacts()
    elif option == "4":
        exit()
    else:
        print("Your input isn't valid, try again.")
        application()


#ADD CONTACT MENU
def AddContact():
    print("Here you can add new contacts")
    print("1. ADD CONTACT")
    print("2. GO BACK")
    option2 = input()
    if option2 == "1":
        print("Please enter datails:")
        name = input("Name: ")
        lastname = input("Lastname: ")
        phone_number = input("Phone number: ")

        with open("contacts.txt", "a") as f:
            f.write(f"Contact {get_contact_number()}\n")
            f.write(f"Name: {name}\n")
            f.write(f"LastName: {lastname}\n")
            f.write(f"Phone number: {phone_number}\n\n")
        print("Contact added successfully!")
        print("1. ADD MORE CONTACTS")
        print("2. GO BACK TO MAIN")
        option3 = input()
        if option3 == "1":
            AddContact()
        elif option3 == "2":
            application()
        else:
            print("Wrong input...Try again later.")



    elif option2 == "2":
        application()
    else:
        print("Wrong input...Try again.")
        AddContact()
#SEE CONTACT MENU
def SeeContacts():
    print("Here you will see all contacts")
    print("1. LIST CONTACTS")
    print("2. GO BACK")
    option2 = input()
    if option2 == "1":
        print("Listing contacts........")
        list_contacts()
    elif option2 == "2":
        application()
    else:
        print("Wrong input...Try again.")
        SeeContacts()
#DELETE CONTACT MENU
def DeleteContacts():
    print("Here you will be able to delete contacts")
    print("1. DELETE CONTACT")
    print("2. GO BACK")
    option2 = input()
    if option2 == "1":
        print("Deleting contact....")
        delete_contacts()
    elif option2 == "2":
        application()
    else:
        print("Wrong input...Try again.")
        DeleteContacts()

def get_contact_number():
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()
            if lines:
                last_contact_line = lines[-5] if len(lines) >= 5 else lines[-len(lines)]
                contact_number = int(last_contact_line.split()[-1]) + 1
            else:
                contact_number = 1
            return contact_number
    except FileNotFoundError:
        return 1
#Listing contacts.
def list_contacts():
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.read()
            print("\n" + contacts)
    except FileNotFoundError:
        print("No contacts found.")

def delete_contacts():
    print("Delete Contacts")
    print("Enter the name of the contact you want to delete:")
    contact_name = input()

   
    if not contact_exists(contact_name):
        print(f"Contact with name '{contact_name}' not found.")
    else:
        remove_contact(contact_name)
        print(f"Contact '{contact_name}' has been deleted.")

def contact_exists(name):
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.read()
            if name in contacts:
                return True
            return False
    except FileNotFoundError:
        return False

def remove_contact(name):
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()

        with open("contacts.txt", "w") as f:
            for line in lines:
                if f"Ime: {name}" not in line:
                    f.write(line)
    except FileNotFoundError:
        pass

application()