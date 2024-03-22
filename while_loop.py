languages = ['c', 'asm', 'python', 'c++', 'rust']

# iterate till the list becomes empty
while languages:
    item = languages.pop()
    print(item)
    
print(f"Languages List: {languages}")
input("Enter to continue... ")

fruits = ['apple', 'orange', 'mango', 'banana', 'apple', 'berry']
# Loop with a specific item only and remove that item
while 'apple' in fruits:
    fruits.remove('apple')
    input("Item removed. Enter to continue... ")
print(f"Fruits List: {fruits}")


# deleting mango using continue and break statements
idx = 0
while fruits:
    fruit = fruits[idx]
    idx = idx + 1
    print(f"Fruit read: {fruit}")
    if fruit != 'mango':
        continue
    else:
        print("deleting mango")
        fruits.remove(fruit)
        break


print(f"Fruits List: {fruits}")



    
