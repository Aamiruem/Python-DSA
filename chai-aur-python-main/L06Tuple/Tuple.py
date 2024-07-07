tea_types = ("Black", "Green", "Oolong")

print(tea_types)

print(tea_types[0])

print(tea_types[-1])
print(tea_types[1:])
print(tea_types[:1])

for tea in tea_types:
    print(tea)
# print(tea_types[0])
# tea_types[0] = "Lemon" #'tuple' object does not support item assignment

print(tea_types[0])


print(len(tea_types))

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types


len(tea_types)

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
if "Green" in all_tea:
    print("I have green tea")

more_tea = ("Herbal", "Earl Grey", "Herbal")
    more tea
('Herbal', 'Earl Grey', 'Herbal')
more_tea.count("Herbal")
2
more_tea.count("Herb")
