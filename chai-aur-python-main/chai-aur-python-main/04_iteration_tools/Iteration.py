myList = [1, 2, 3, 4, 5]
I = iter(myList)
print(I)


print(I.__next__())

print(I)


print(I.__next__())
print(I)


print(I.__next__())
print(I)


print(I.__next__())


# f = open('chai.py')
# iter(f) is f
# print(f)

# iter(f) is f.__iter__()


# myNewList = [1, 2, 3]
# print(iter(myNewList) is myNewList)


D = {'a': 1, 'b':2}
for key in D.keys():
    print(key)

I = iter(D)
print(I)

print(next(I))

print(next(I))


range(5)
range(0, 5)
R = range(5)
print(R)

I = iter(R)
print(next(I))

print(next(I))

print(next(I))

print(next(I))

