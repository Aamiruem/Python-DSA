chai_types = {"masala": 'spicy', 'Ginger': 'zesty', 'Green': 'Mild' 
    }


print(chai_types)

print(chai_types["masala"])

print(chai_types)


for chai in chai_types:
    print(chai, chai_types[chai])




for key, value in chai_types.items():
    print(key, value)


if "Masala" in chai_types:
    print("I masala chai")

print(chai_types)


chai_types["Earl Grey"] = "citrus"
print(chai_types)

print(chai_types.pop("Ginger"))

print(chai_types)
default_value = "Delicious"
new_dict = dict.fromkeys(key, default_value)
print(new_dict)


new_dict = dict.fromkeys(key, key)
print(new_dict)
