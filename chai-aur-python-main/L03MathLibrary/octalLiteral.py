# x = 0o20
# print(x)
# # output is 16

# y = 0xff
# print(y)
# # output is 255


# x = 0b1000
# print(x)
# # output is 8

# octal = oct(64)
# print(octal)
# # output is 0o100


# hex = hex(64)
# print(hex)
# # output is 0x40


# bin = bin(64)
# print(bin)
# # output is 0b1000000


# x = int(3.14)
# print(x)


# x = float(314)
# print(x)


# x = bool(3.14)
# print(x)


# x != bool(3.14)
# print(x)


# x = int('64',  8)
# print(x)


# x = int('64',  16)
# print(x)

# x = int('10000',  2)
# print(x)

# x = 1
# print(x<<2)



# import random

# # Generate a random integer between 1 and 100

# random_integer = random.randint(1, 100)
# print(random_integer)

# l1 = ['lemon', 'masala', 'ginger', 'mint']

# print(random.choice(l1))



# l1 = ['Biryani', 'motton', 'polaw', 'Rice']
# r = random.choice(l1)
# print(r)


# x = 0.1 + 0.1 + 0.4

# print(x)



# x = 0.1 + 0.1 + 0.1 - 0.4

# print(x)
# # output -0.09999999999999998


# x = (0.1 + 0.1 + 0.1) - 0.4

# print(x)
# # output -0.09999999999999998


# import math
# x = (0.1 + 0.1 + 0.1) - 0.4
# print(x)



# # This is a correct way to find it
# from decimal import Decimal
# x = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')

# print(x - Decimal('0.4'))


# from fractions import Fraction

# x = Fraction(0.1) + Fraction(0.1) + Fraction(0.1)

# print(Fraction(x))



# from fractions import Fraction

# x = Fraction(2, 7)

# print(Fraction(x))




#----------------------------#

set1 = {1, 2, 3, 4}
print(set1&{1, 3})


print(set1 | {1, 3})

print(set1 | {1, 3, 7})

set2 = set1 - {1, 2, 3, 4}
print(set2)

print(type({}))
# output set()
# output <class 'dict'>
print(type(set1))

