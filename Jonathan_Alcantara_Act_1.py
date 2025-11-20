#Python Test
print("Hello")
print(100)
print(" ")

#Print methods
print("Hello World".lower())
print("Hello World".upper())
print("Hello World".swapcase())
print("Hello World".replace("World", ", Goodbye"))

print(" ")

#Setting Value of Variables
a="I love you"
b=3000

#concatenation
print(a,b)
print(a.upper(),b)
print(" ")

#Arithmetic Operators (+,-,*,/ (float), // (no decimal), % (modulo), ** (exponent))
numOne=5
numTwo=5

print(numOne+numTwo)
print(numOne-numTwo)
print(numOne*numTwo)
print(numOne/numTwo)
print(numOne//numTwo)
print(numOne%numTwo)
print(numOne**numTwo)
print(numOne+numTwo-numOne*numTwo/numOne//numTwo%numOne**numTwo)

#Taking Input From User
print("\nHello Good Day!")

name=input("Enter Your Name: ")
age=input("Enter Age: ")
address=input("Enter Address: ")
gender=input("Enter Gender(F/M): ")

print("Hello", name, "\t\tAge:", age, "\tAddress:", address, "\tGender:", gender)

#Comparison Operators (==, !=, >, <, >=, <=)
if 5 == 5:
    print("true")
else:
    print("false")
    
if 5 != 5:
    print("true")
else:
    print("false")
    
if 5 > 5:
    print("true")
else:
    print("false")
    
if 5 < 5:
    print("true")
else:
    print("false")
    
if 5 >= 5:
    print("true")
else:
    print("false")
    
if 5 <= 5:
    print("true")
else:
    print("false")
    
if 5 == 5:
    print("\ntrue")
elif 3 != 5:
    print("true")
else:
    print("ERROR")
    
#Check Data Type
name2 = str("jay")
age = int(9)
grade = float(89)
BoolVar = bool("true")
fruit_list = ["mango", "grape", "orange"]

print(type(name2))
print(type(age))
print(type(grade))
print(type(BoolVar))

print(fruit_list[0])