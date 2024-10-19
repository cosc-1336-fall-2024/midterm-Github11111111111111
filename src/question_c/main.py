#add import
def reverse_string(string1):
    reversed_string = ""
    index = len(string1) - 1  
    
    while index >= 0:  
        reversed_string += string1[index]  
        index -= 1  
    
    return reversed_string

def main():
    while True:
        user_input = input("Enter a string to reverse (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        reversed_value = reverse_string(user_input)
        print(f"Reversed string: {reversed_value}")

if __name__ == "__main__":
    main()
