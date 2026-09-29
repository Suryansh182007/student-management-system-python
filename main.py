# main.py

import file_handler
import records
import display
import menu

def main():
    # 1. Program shuru hote hi purana data load karo
    all_records = file_handler.load_records()
    
    while True:
        choice = menu.display_menu()
        
        if choice == "1":
            records.add_records(all_records)
            
        elif choice == "2":
            records.search_student(all_records)
            
        elif choice == "3":
            records.update_student(all_records)
            
        elif choice == "4":
            records.delete_student(all_records)
            
        elif choice == "5":
            display.show_all(all_records)
            
        elif choice == "6":
            print("\nExiting program... Good bye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Main function ko chalao
main()