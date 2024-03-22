mylist = [ 'apple', 'mango', 'banana', 'tomato', 'jackfruit', 'blueberry', 'orange' ]
for fruit in mylist:
    print(fruit)

for value in range(0, 5):
    print(value)

# range with step of 3
for value in range(1, 15, 3):
    print(value)

mylist1 = list(range(1,15,3))
for value in mylist1:
    print(value)

print(min(mylist1))
print(max(mylist1))
print(sum(mylist1))

# list comprehensions
squares = [value**2 for value in mylist1]
print(squares)

# slices
sl_list = list(range(0, 21))
print(sl_list)

print("*****************")
print(sl_list[0:3]) # first 3 elements
print(sl_list[:]) # entire list
print(sl_list[:3]) # from first element, 3 elements
print(sl_list[2:10]) # from 3rd element, 8 elements
print(sl_list[-5:]) # last 5 elements


# copying a list
new_list = sl_list[:]
# address of above lists will be different
print(f"id of sl_list is {id(sl_list)}")
print(f"id of new_list is {id(new_list)}")

# referencing list with another variable
ref_sl_list = sl_list
# address of above lists will be same
print(f"id of sl_list is {hex(id(sl_list))}")
print(f"id of ref_sl_list is {hex(id(ref_sl_list))}")

# similarly for a simple variable
from ctypes import c_int, addressof
mydata = 454
print(f"address of mydata is {addressof(c_int(mydata))}")

