items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)
    
    
    
    
    
    
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Example usage
numbers = [1, 2, 3, 4, 2, 5, 6, 1, 3]
print("Duplicates in the list:", find_duplicates(numbers))




def find_duplicates(nums):
    count_dict = {}
    duplicates = []
    
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for num, count in count_dict.items():
        if count > 1:
            duplicates.append(num)
    
    return duplicates

# Example usage
items = ["apple", "banana", "orange", "apple", "mango"]
print("Duplicates in the list:", find_duplicates(items))



from collections import Counter

def find_duplicates(nums):
    count = Counter(nums)
    duplicates = [num for num, cnt in count.items() if cnt > 1]
    return duplicates

# Example usage
numbers = [1, 2, 'aam', 4, 'aam', 2, 5, 'kamran', 'kamran', 3]
print("Duplicates in the list:", find_duplicates(numbers))
