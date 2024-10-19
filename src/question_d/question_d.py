#write functions here, don't add input('') statements here!
def use_local_variable(num):
    num = 10
    print("Inside the function, local num =", num)

global_num = 5
print("Before calling the function, global_num =", global_num)

use_local_variable(global_num)

print("After calling the function, global_num =", global_num)

