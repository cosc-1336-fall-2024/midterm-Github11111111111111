#add import
def use_local_variable(num):
    num = 10
    print("Inside the function, local num =", num)

num = 5  
print("Before calling the function, num =", num)

use_local_variable(num)

print("After calling the function, num =", num)
