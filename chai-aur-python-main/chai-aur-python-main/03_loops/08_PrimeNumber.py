number = 23

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)




def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input from the user
limit = int(input("Enter the upper limit to find prime numbers: "))

# Loop to find and print prime numbers
print(f"Prime numbers up to {limit} are:")
for number in range(2, limit + 1):
    if is_prime(number):
        print(number, end=' ')
