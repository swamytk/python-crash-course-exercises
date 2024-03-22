mylist = [45, 5,100, -1, 2394, 0, 0, -300, 94]
print(mylist)

# last element
print(mylist[-1])
# last but one
print(mylist[-2])

mylist.append(555)
print(mylist[-1])

print(len(mylist))

mylist.insert(1,444)
print(mylist)

del mylist[2]
print(mylist)

last_val = mylist.pop()
print(last_val)
print(mylist)

last_but_one = mylist.pop(-2)
print (last_but_one)
print(mylist)

mylist.remove(2394)
print(mylist)

# permanent sort
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)

# temporary sort
print(sorted(mylist))
print(mylist)

# permanently reverse order the list elements
mylist.reverse()
print(mylist)
