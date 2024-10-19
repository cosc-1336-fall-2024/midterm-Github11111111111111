#add import
def get_bonus_pay_amount(sales):
    if sales < 0 or sales > 1999:
        return "Invalid arguments"
    
    if sales < 500:
        bonus_percentage = 0.05
    elif sales < 1000:
        bonus_percentage = 0.06
    elif sales < 1500:
        bonus_percentage = 0.07
    else:  # sales is between 1500 and 1999
        bonus_percentage = 0.08

    bonus_amount = sales * bonus_percentage
    return bonus_amount

# Prompt the user for sales amount
try:
    sales_input = float(input("Enter the sales amount: "))
    bonus = get_bonus_pay_amount(sales_input)
    print(f"The bonus pay amount for sales of {sales_input} is: {bonus}")
except ValueError:
    print("Please enter a valid number.")
200