

import file_handler
import display

def add_records(records):
    reg_no = input("enter registration number : ")
    if reg_no in records:
        print("student already exists!")
        return
        
    name = input("enter name : ")
    hostel = input("enter hostel : ")
    state = input("enter state : ")
    email = input("enter email : ")
    contact = input("enter contact : ")

    records[reg_no] = {
        "name": name,
        "hostel_block": hostel,
        "state": state,
        "email": email,
        "contact": contact
    }
    
    file_handler.save_records(records)
    print("student added successfully!")


def search_student(records):
    reg_no = input("enter registration number : ")
    if reg_no not in records:
        print("no student found ")
        return False
    else:
        print("found student!")
        display.show_student(reg_no, records[reg_no])
        return True


def update_student(records):
    reg_no = input("enter registration number to update: ")
    if reg_no not in records:
        print("student not found!")
        return
        
    print("enter new details:")
    name = input("enter name : ")
    hostel = input("enter hostel : ")
    state = input("enter state : ")
    email = input("enter email : ")
    contact = input("enter contact : ")

    records[reg_no] = {
        "name": name,
        "hostel_block": hostel,
        "state": state,
        "email": email,
        "contact": contact
    }
    file_handler.save_records(records)
    print("record updated successfully!")


def delete_student(records):
    reg_no = input("enter registration number to delete: ")
    if reg_no not in records:
        print("student not found!")
        return
        
    del records[reg_no]
    file_handler.save_records(records)
    print("student deleted successfully!")