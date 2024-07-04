chai = 'masala chai'
print(chai)

slice_chai = chai[0:6]

print(slice_chai)

num_list = "0123456789"
print(num_list[3:])

print(num_list[:7])

print(num_list[0:7:2])

print(num_list[0:7:3])

print(num_list[-1:])

print(num_list[7:-1])

print(num_list[0:-1])

tea = 'Masala Chai'
print(tea.lower())
print(tea.upper())

print(chai)



chai = "  Masala Chai   "
print(chai)


chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))


chai = "Masala Chai"
print(chai.find("Chai"))


print(chai.find("mango"))

# counting chai
chai = "masala chai chai chai chai"
print(chai.count("chai"))

print(chai.count("a"))

print(chai.count("i"))

print(chai.count("e"))



chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(f"You ordered {quantity} {chai_type} chai.")

print(order.format(quantity, chai_type))


chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety)

print("".join(chai_variety))

print(" ".join(chai_variety))

print("_".join(chai_variety))

print("-".join(chai_variety))

print(", ".join(chai_variety))


print(len(chai))


chai = "Masala Chai"
for letter in chai:
    print(letter)


chai = "He said, \"Masala chai is awesome\" "
print(chai)

chai = 'He said, "Masala chai is awesome"'
print(chai)


chai = "MASALA\nChai"
print(chai)

chai = r"Masala\nchai"
print(chai)


chai = r"c:\\user\\pwd\\"
print(chai)


chai = r"c:\user\pwd"

print(chai)


chai = 'c:\\user\\pwd'

print(chai)
