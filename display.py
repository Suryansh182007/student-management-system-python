# display.py

def show_student(records):
    reg_no = input("enter registration number to show details: ")
    
    if reg_no not in records:
        print("no student found with this registration number!")
        return
        
    info = records[reg_no]
    
    # Header line
    print("\n" + "="*80)
    print(f"{'REG NO':<12} | {'NAME':<25} | {'HOSTEL':<10} | {'STATE':<25} | {'EMAIL':<30} | {'CONTACT':<15}")
    print("="*117)
    
    # Data row
    print(f"{reg_no:<12} | {info['name']:<25} | {info['hostel_block']:<10} | {info['state']:<25} | {info['email']:<30} | {info['contact']:<15}")
    print("="*117 + "\n")


def show_all(records):
    if records == {}:
        print("no records found!")
        return

    print("\n" + "="*117)
    # Header
    print(f"{'REG NO':<12} | {'NAME':<25} | {'HOSTEL':<10} | {'STATE':<25} | {'EMAIL':<30} | {'CONTACT':<15}")
    print("="*117)
    
    # Sabhi students ki row print karega
    for reg_no in records:
        info = records[reg_no]
        print(f"{reg_no:<12} | {info['name']:<25} | {info['hostel_block']:<10} | {info['state']:<25} | {info['email']:<30} | {info['contact']:<15}")
        
    print("="*117 + "\n")