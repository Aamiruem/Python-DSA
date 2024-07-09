def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# Taking user input
number = int(input("Enter a number: "))

# Calculating the factorial of the number
result = fact(number)

# Printing the result
print(f"The factorial of {number} is {result}")









def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
