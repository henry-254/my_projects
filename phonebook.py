phonebook = {}

def add_contact(name, phone_number):
    if name in phonebook:
        print(f"{name} already exists in the phonebook.")
    else:
        phonebook[name] = phone_number
        print(f"{name} was added to the phonebook.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} was deleted from the phonebook.")
    else:
        print(f"{name} does not exist in the phonebook.")

def search_contact(name):
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}.")
    else:
        print(f"{name} does not exist in the phonebook.")

def display_phonebook():
    print("Phonebook:")
    for name, phone_number in phonebook.items():
        print(f"{name}: {phone_number}")

while True:
    print("\nOptions:")
    print("1. Add a contact")
    print("2. Delete a contact")
    print("3. Search for a contact")
    print("4. Display phonebook")
    print("5. Quit")

    choice = input("Enter an option number: ")

    if choice == "1":
        name = input("Enter a name: ")
        phone_number = input("Enter a phone number: ")
        add_contact(name, phone_number)
    elif choice == "2":
        name = input("Enter a name: ")
        delete_contact(name)
    elif choice == "3":
        name = input("Enter a name: ")
        search_contact(name)
    elif choice == "4":
        display_phonebook()
    elif choice == "5":
        break
    else:
        print("Invalid option. Please enter a number from 1 to 5.")
