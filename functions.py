def function1(name):
    print(f"Name is {name}")

function1("Swamy")

# default values
def function2(name, greetings="Hi, Friend"):
    print(f"{greetings}, {name}")

function2('Swamy')
function2('Swamy', "How are you?")

# return value
def my_sum(a,b):
    return (a+b)

print(f"Sum is {my_sum(10,5)}")

# Optional arguments
def function3(name, title=''):
    print(f"{title} {name}")

function3('Swamy')
function3('Swamy', 'Mr.')

# Passing a list (modifiable)
name_list = ['Swamy', 'Kumar', 'Peter', 'Ganesh', 'Ram', 'Ismail']
def function4(mylist):
    mylist.remove('Swamy')

function4(name_list)
print(name_list)

# Passing a copy of list
name_list1 = ['Swamy', 'Kumar', 'Peter', 'Ganesh', 'Ram', 'Ismail']
def function5(mylist):
    mylist.remove('Swamy')
    print(mylist)

function5(name_list1[:])
print(name_list1)

# Passing an arbitrary number of arguments - Tuple
def print_food(*food):
    print(food[len(food)-1])
    # Tuple can't be modified, the below statement will throw error
    #food[0] = 'poha'

print_food('idli')    
print_food('dosa', 'uththappam', 'poori')

# Passing an arbitrary number of arguments (Tuple ) along with positional argument
def print_food(drink, *food):
    print(drink)
    print(food[len(food)-1])
    # Tuple can't be modified, the below statement will throw error
    #food[0] = 'poha'

print_food('coffee', 'idli')    
print_food('boost', 'dosa', 'uththappam', 'poori')

# Passing arbitrary number of keyword arguments
def print_components(cpu, motherboard, **others):
    print(cpu)
    print(motherboard)
    print(others)
    
print_components('ryzen 5900x', 'gigabyte b550 aorus elite ax', 
        ram = 'corsair ddr4 3200',
        storage = 'Kingston KC3000',
        gpu = 'asus tuf rtx 4090'
    )

# The below should throw error since third argument (dict) is considered as 
#   positional argument when you pass a dictionary
#print_components('ryzen 5900x', 'gigabyte b550 aorus elite ax', 
#        { 
#            'ram' : 'corsair ddr4 3200',
#            'storage' : 'Kingston KC3000',
#            'gpu' : 'asus tuf rtx 4090'
#        }
#    )

# various ways to import a module
import mymodule
print(my_sum(3,4))

# import a specific function
#from mymodule import my_div
from mymodule import my_div, my_mult
# import all functions
#from mymodule import *
print(my_div(30,3))

# alias for module
import mymodule as arith
print(arith.my_sum(4,5))
print(arith.my_pi)
# data from module is modifiable
arith.my_pi = 3.14
print(arith.my_pi)
















