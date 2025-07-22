def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Unknown operation"
print(calculate(10, 5, "add"))       
print(calculate(10, 5, "subtract"))  
print(calculate(10, 5, "multiply"))  
print(calculate(10, 5, "divide"))    
print(calculate(10, 5, "modulus"))    
