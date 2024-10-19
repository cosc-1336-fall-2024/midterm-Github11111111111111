#add import
def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes <= 0:
        return 'Invalid arguments'
    
    miles = kilometers * 0.621371
    
    hours = minutes / 60
    
    miles_per_hour = miles / hours
    
    return miles_per_hour

if __name__ == "__main__":
    try:
        kilometers = int(input("Enter kilometers: "))
        minutes = int(input("Enter minutes: "))
        
        result = get_miles_per_hour(kilometers, minutes)
        
        print("Miles per hour:", result)
        
    except ValueError:
        print("Please enter valid integers for kilometers and minutes.")
