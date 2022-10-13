# Variables
# do not declare variables. No semicolons are the end of lines
name = "Alvin"
last_name = "Burgos" 
age = 40
price = 12.31
found = False 

print(name)
print(last_name)

print(name + last_name) # string concatenation
print(21 + 21)

# print(21 + name)

# math operands
print(21 * 21)

# if statements
if(age < 100): # colon used. NO parenthesis
    print("Don't worry, you are still young")   # lines that are indented the same amount are within the same block
    print("Inside the if")
    print("Inside the if")
elif age == 100:  # elif is short for else if.
    print("Congrats on the century")
else:  # else statement must match with initial if statement
    print("Sorry bud, you are getting old")

print("outside the if")  # line is indented differently, outside of if statement.


def test():
    print("I'm a function")

def say_hello(name):
    print("Hello there " + name)

def sum(num1, num2):
    return num1 + num2


test() # call/execute a function
test() # function can be called mutliple times to be reusable
test()

say_hello("Bart")

result = sum(21, 21)
print("The result of the sum is: " + str(result))

