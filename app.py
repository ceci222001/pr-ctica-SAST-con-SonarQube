# app.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

print("Suma:", suma(5, 3))
print("Resta:", resta(5, 3))
print("División:", division(5, 0))
