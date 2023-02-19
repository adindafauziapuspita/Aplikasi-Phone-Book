import os
import re

contact={}

def menu():
    print("+=========================+")
    print("+        Phone Book       +")
    print("+=========================+")
    print("+    1. Add contact       +")
    print("+    2. Display Contact   +")
    print("+    3. Update Contact    +")
    print("+    4. Delete Contact    +")
    print("+    5. Search Contact    +")
    print("+    0. Back              +")
    print("+=========================+")
    choose = input("choose : ")
    return choose 

def add_contact():
    global contact
    name = input("Name : ")
    phone = input("Phone : ")
    contact[name] = phone
    file = open("Phonebook.txt", "a")
    file.write(name + " : " + phone + "\n")
    file.close()
    print("Contact added successfully!")

def display_contact():
    file = open("Phonebook.txt", "r")
    print(file.read())
    file.close()

def update_contact():
    Choose = input("What do you want to update(Name/Number) ? ")
    if Choose == "Name" or Choose == "name":
        upd2 = open("Phonebook.txt", "r")
        old_name = input ("Enter old name : ")
        new_name = input ("Enter new name : ")
        s = re.sub(old_name, new_name, upd2.read())

        upd1 = open("Phonebook.txt", "w")
        upd1.writelines(s)
        print("Name update successfully!")
        upd2.close()
        upd1.close()
    elif Choose == "Number" or Choose == "number":
        upd2 = open("Phonebook.txt", "r")
        old_number = input ("Enter old number : ")
        new_number = input ("Enter new number : ")
        s = re.sub(old_number, new_number, upd2.read())

        upd1 = open ("Phonebook.txt", "w")
        upd1.writelines(s)
        print("Number update successfully!")
        upd2.close()
        upd1.close()
    else:
        print("It's wrong input!")
        input()

def del_contact():
    name = input("Name: ")
    file = open("PhoneBook.txt", "r")
    lines = file.readlines()
    file = open("PhoneBook.txt", "w")
    found = False
    for line in lines:
        if not name.lower() in line.lower():
            file.write(line)
        else:
            found = True
    if found:
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def search_contact():
    nama = input("Input Name : ")
    with open("PhoneBook.txt", "r") as file:
        for line in file:
            if nama in line:
                print(line)
                return
        print("Name not found!")
   
while True:
    match menu():
        case "1":
            add_contact()
        case "2":
            display_contact()               
        case "3":
            update_contact()
        case "4":
            del_contact()
        case "5":
            search_contact()
        case "0":
            print("Thank you for using our phone book!")
        case _:
            print("Invalid input! Please try again.")


            