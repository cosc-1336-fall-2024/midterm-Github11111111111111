#write functions here, don't add input('') statements here!
def get_bonus_pay_amount(sales):
    if sales < 0 or sales > 1999:
        return "Invalid arguments"
    
    if sales < 500:
        bonus_percentage = 0.05
    elif sales < 1000:
        bonus_percentage = 0.06
    elif sales < 1500:
        bonus_percentage = 0.07
    else:  
        bonus_percentage = 0.08

    bonus_amount = sales * bonus_percentage
    return bonus_amount




