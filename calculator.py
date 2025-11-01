def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multipy(a,b):
    return a * b
def devide(a,b):
    if b == 0:
        return "Error : Division by zero"
    return a / b

def calculator():
    print("Welcome to the Calculator!")
    
    while True:
    
        user_input = input("Enter operation (eg : 7+3)) : ")
        
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        try:
            num1,op,num2 = user_input.split()
            num1 = float(num1)
            num2 = float(num2)
            
            if op == '+':
                result = add(num1,num2)
            elif op == '-': 
                result = sub(num1,num2) 
            elif op == '*':
                result = multipy(num1,num2)
            elif op == '/':
                result = devide(num1,num2)
            
            else:
                print("Invalid operation. Please use +, -, *, or /.")
                continue
            
            print(f"The result is: {result}")
            
        except ValueError:
            print("Invalid input format. Please enter in the format: number1 operator number2 (e.g., 7 + 3).")
            continue    
        
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
    
if __name__ == "__main__":
    calculator()

