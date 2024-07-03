# myListOne = [1, 2, 3, 4, 5]
# myListTwo = myListOne

# myListTwo.append(6)

# print(myListTwo)

# print(myListOne)

# print(myListTwo is myListOne)

# print(myListTwo == myListOne)

# print(myListTwo.count(1))

# myListTwo = [1, 2, 3, 4, 5]


# l1 = [1, 2, 3, 4]
# l2 = l1
# print(l1)

# print(l2)

# l1[0] = 44
# print(l2)

# magic
p1 = [1, 2, 3]
p2 = p1
p2 = [1, 2, 3]
p1[0] = 55
print("This is p1 which is change  = ", p1)

print("This is p2 which is not change  = ", p2)





h1 = [1, 2, 3]
h2 = h1[:]
print(h1)

h2 = h1[1:2]
print(h1)

print(h2)

# deepcopy means list ke andar wala list ka copy le aao

import copy
h2 = copy.deepcopy(h1)



n = [1, 2, 3]
m = n
print(m)

m = [1, 2, 3]
m == n

m is n

n = [1, 2, 3]
m == n

m = [1, 2, 3]
m == n

m is n

