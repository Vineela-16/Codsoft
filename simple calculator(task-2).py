#Simple Calculator
 
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        print( "Error! Division by zero is not possible.")
    else:
        return x / y

    

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nSelect an operation:")
print("~~~~~~~~~~~~~~~~~")
print("1. Addition",end="   ")
print("2. Subtraction",end="   ")
print("3. Multiplication",end="   ")
print("4. Division\n")

    
choice = input("\nEnter your choice : ")
if choice == '1':
    print("Sum of", num1 ,"and", num2," =", add(num1, num2))
      
elif choice == '2':
    print("Difference between ",num1 ,"and", num2," =", sub(num1, num2))
        
elif choice == '3':
    print("Product of ",num1 ,"and", num2," =",mul(num1, num2))
        
elif choice == '4':
    print("Quotient of",num1 ,"and", num2," =", div(num1, num2))
        
else:
    print("Invalid input")
