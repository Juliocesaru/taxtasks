def calculate_federal_tax(income):
    federal_brackets = [
        (53359, 0.15),
        (53359, 0.205),
        (58197, 0.26),
        (69695, 0.29),
        (float('inf'), 0.33)
    ]
    
    federal_tax = 0
    for bracket in federal_brackets:
        if income > bracket[0]:
            federal_tax += bracket[0] * bracket[1]
            income -= bracket[0]
        else:
            federal_tax += income * bracket[1]
            break
    return federal_tax

def calculate_provincial_tax_ontario(income):
    provincial_brackets = [
        (47630, 0.0505),
        (47629, 0.0915),
        (12579, 0.1116),
        (21523, 0.1216),
        (float('inf'), 0.1316)
    ]
    
    provincial_tax = 0
    for bracket in provincial_brackets:
        if income > bracket[0]:
            provincial_tax += bracket[0] * bracket[1]
            income -= bracket[0]
        else:
            provincial_tax += income * bracket[1]
            break
    return provincial_tax

def calculate_provincial_tax_quebec(income):
    provincial_brackets = [
        (49275, 0.15),
        (49275, 0.20),
        (19310, 0.24),
        (float('inf'), 0.2575)
    ]
    
    provincial_tax = 0
    for bracket in provincial_brackets:
        if income > bracket[0]:
            provincial_tax += bracket[0] * bracket[1]
            income -= bracket[0]
        else:
            provincial_tax += income * bracket[1]
            break
    return provincial_tax

def calculate_provincial_tax_alberta(income):
    provincial_brackets = [
        (142292, 0.10),
        (26145, 0.12),
        (52291, 0.13),
        (104573, 0.14),
        (float('inf'), 0.15)
    ]
    
    provincial_tax = 0
    for bracket in provincial_brackets:
        if income > bracket[0]:
            provincial_tax += bracket[0] * bracket[1]
            income -= bracket[0]
        else:
            provincial_tax += income * bracket[1]
            break
    return provincial_tax

def main():
    income = float(input("Enter your annual income: "))
    
    federal_tax = calculate_federal_tax(income)
    
    province = input("Enter your province (Ontario, Quebec, Alberta): ").strip().lower()
    if province == "ontario":
        provincial_tax = calculate_provincial_tax_ontario(income)
    elif province == "quebec":
        provincial_tax = calculate_provincial_tax_quebec(income)
    elif province == "alberta":
        provincial_tax = calculate_provincial_tax_alberta(income)
    else:
        print("Invalid province entered.")
        return
    
    total_tax = federal_tax + provincial_tax
    
    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"Provincial Tax: ${provincial_tax:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")

if __name__ == "__main__":
    main()
