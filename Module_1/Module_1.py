# Problem 1: Write a program that takes a number and checks if it is even or odd


num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")




# Problem 2: Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")


if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operator")




# Problem 3: Sum of Even Numbers from 1 to 100
total = 0

for i in range(2, 101, 2):                    # Start from 2  to 100, step by 2
    total += i

print("Sum of even numbers between 1 and 100 is:", total)