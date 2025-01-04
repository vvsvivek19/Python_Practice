import json

# Sample phonebook dictionary
phonebook = {
    "John Doe": {
        "phone": "123-456-7890",
        "email": "johndoe@example.com",
        "address": "123 Elm Street, Springfield"
    },
    "Jane Smith": {
        "phone": "987-654-3210",
        "email": "janesmith@example.com",
        "address": "456 Oak Avenue, Metropolis"
    }
}

# Function to add a new entry
def add():
    details = ['phone', 'email', 'address']
    new_entry = dict.fromkeys(details)
    name = input("Enter the name: ")
    new_entry['phone'] = input("Enter phone number in format NNN-NNN-NNNN: ")
    new_entry['email'] = input("Enter email ID: ")
    new_entry['address'] = input("Enter Address: ")
    phonebook[name] = new_entry
    print("Entry added successfully!")
    print(json.dumps(phonebook, indent=4))

# Function to update an existing entry
def update():
    name = input("Enter the name: ")
    if name in phonebook:
        field = input("What do you want to update (phone/email/address): ")
        if field in phonebook[name]:
            phonebook[name][field] = input("Please enter the new details: ")
            print("Entry updated successfully!")
        else:
            print("Invalid field. Choose from phone, email, or address.")
    else:
        print("Name not found in the phonebook.")
    print(json.dumps(phonebook, indent=4))

# Function to delete an existing entry
def delete():
    name = input("Enter the name: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted entry for {name}.")
    else:
        print("Name not found in the phonebook.")
    print(json.dumps(phonebook, indent=4))

# Function to search for an entry
def search():
    name = input("Enter the name: ")
    if name in phonebook:
        print("Details are:")
        print(json.dumps(phonebook[name], indent=4))
    else:
        print("Name not found in the phonebook.")

# Main menu function
def menu():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add a new entry")
        print("2. Update an existing entry")
        print("3. Delete an entry")
        print("4. Search for an entry")
        print("5. View entire phonebook")
        print("6. Exit")
        
        # Prompt the user for a choice
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add()
        elif choice == "2":
            update()
        elif choice == "3":
            delete()
        elif choice == "4":
            search()
        elif choice == "5":
            print("Current Phonebook:")
            print(json.dumps(phonebook, indent=4))
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the menu
menu()
