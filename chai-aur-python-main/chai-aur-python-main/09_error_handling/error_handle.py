file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('chai aur python')
    






# for i in enumerate(list, start=1):
#     print(i)

# (1, {"name": "chai", "time": "2min"})
# (2, {"name": "code", "time": "3min"})
# (3, {"name": "python", "time": "4min"})
# for i, video in enumerate(list, start=1):
#     print(f"{i}, {video[name]}")






# Sample list of dictionaries
video_list = [
    {'name': 'chai', 'time': '2min'},
    {'name': 'code', 'time': '3min'},
    {'name': 'python', 'time': '4min'}
]

# Outer loop to print the entire dictionary
for i, video in enumerate(video_list, start = 1):
    print(i, video)

print("\n")  # Adding a newline for clarity

# Inner loop to print the index and the value of the 'name' key
for i, video in enumerate(video_list, start = 1):
    print(f"{i}, {video['name']}")
