FEDERAL_BRACKETS = [53359, 53359, 58197, 69695, float('inf')]
FEDERAL_RATES = [0.15, 0.205, 0.26, 0.29, 0.33]

ONTARIO_BRACKETS = [47630, 47629, 12579, 21523, float('inf')]
ONTARIO_RATES = [0.0505, 0.0915, 0.1116, 0.1216, 0.1316]

QUEBEC_BRACKETS = [49275, 49275, 19310, float('inf')]
QUEBEC_RATES = [0.15, 0.20, 0.24, 0.2575]

ALBERTA_BRACKETS = [142292, 26145, 52291, 104573, float('inf')]
ALBERTA_RATES = [0.10, 0.12, 0.13, 0.14, 0.15]

def calculate_tax(income, brackets, rates):
    tax = 0
    for i in range(len(brackets)):
        if income > brackets[i]:
            tax += brackets[i] * rates[i]
            income -= brackets[i]
        else:
            tax += income * rates[i]
            break
    return tax

def main():
    income = float(input("Enter your annual income: "))
    
    federal_tax = calculate_tax(income, FEDERAL_BRACKETS, FEDERAL_RATES)
    
    province = input("Enter your province (Ontario, Quebec, Alberta): ").strip().lower()
    if province == "ontario":
        provincial_tax = calculate_tax(income, ONTARIO_BRACKETS, ONTARIO_RATES)
    elif province == "quebec":
        provincial_tax = calculate_tax(income, QUEBEC_BRACKETS, QUEBEC_RATES)
    elif province == "alberta":
        provincial_tax = calculate_tax(income, ALBERTA_BRACKETS, ALBERTA_RATES)
    else:
        print("Invalid province entered.")
        return
    
    total_tax = federal_tax + provincial_tax
    
    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"Provincial Tax: ${provincial_tax:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")

if __name__ == "__main__":
    main()

