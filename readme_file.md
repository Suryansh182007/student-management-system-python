# Student Management System

This is a simple Python project for managing student records. It stores student information in a text file so that data remains saved even after closing the program.

## Project Structure
- `main.py` - The main starting file of the program.
- `menu.py` - Handles showing the selection menu on terminal.
- `records.py` - Contains core functions for adding, searching, updating, and deleting records.
- `file_handler.py` - Reads from and writes data to the file.
- `display.py` - Formats and prints student data neatly.
- `config.py` - Contains settings like the file path/name.
- `records.txt` - Text file storing student details line by line.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Place all `.py` files and `records.txt` in the same directory.
3. Open terminal/cmd in that directory and run:

```bash
python main.py
```

## Features
- **1. Add Student:** Add new registration number, name, hostel block, state, email, and contact number.
- **2. Search Student:** Search for a student by entering their registration number.
- **3. Update Student:** Modify existing student information.
- **4. Delete Student:** Remove student record from system.
- **5. Show All:** View table list of all students.
- **6. Exit:** Save and quit the program.