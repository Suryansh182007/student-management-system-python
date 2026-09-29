

import config

def save_records(records):
    f = open(config.FILENAME, "w")
    
    for reg_no in records:
        info = records[reg_no]
        line = reg_no + " | " + info["name"] + " | " + info["hostel_block"] + " | " + info["state"] + " | " + info["email"] + " | " + info["contact"] + "\n"
        f.write(line)
        
    f.close()


def load_records():
    records = {}
    try:
        f = open(config.FILENAME, "r")
        lines = f.readlines()
        f.close()
        
        for line in lines:
            line = line.strip()
            if line != "":
                items = line.split(" | ")
                reg_no = items[0]
                records[reg_no] = {
                    "name": items[1],
                    "hostel_block": items[2],
                    "state": items[3],
                    "email": items[4],
                    "contact": items[5]
                }
    except:
        pass
        
    return records