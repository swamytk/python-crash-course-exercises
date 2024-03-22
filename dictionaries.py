resume = {
    'name' : "Swamy",
    'age' : 52
}
print(resume)

# adding key-pair
resume['education'] = 'AMIE(I)'
resume['place'] = 'Pune'
print(resume)

# modifying value
resume['name'] = "KaruppuSwamy"

# removing a pair
del resume['place']
print(resume)

# read a value
print(resume['age'])

# read a invalid key-value without exception handling
#my_college = resume['college']

# read a invalid key-value with exception handling
my_college = resume.get('college', 'No such key')
print(my_college)
# read a invalid key-value with special None value
my_college = resume.get('college')
print(my_college)

# Looping key-value pair
for item in resume.items():
    print(item)

# Looping keys only
for item in resume.keys():
    print(item)
# Looping keys only in sorted    
for item in sorted(resume.keys()):
    print(item)

# Looping values only
for item in resume.values():
    print(item)

# List of dictionaries
recruitment = [
    resume,
    { "interviewer" : "Gupta", 'selected' : True }
]
print(recruitment)

# List in a dictionary
resume['languages'] = ['c', 'python']
print(resume)

# Dictionary in a Dictionary
users = {
    'Swamy' : {
        'first_name' : 'KaruppuSwamy',
        'education' : 'AMIE(I)'
    },
    'Sangeetha' : {
        'first_name' : 'Sangeetha',
        'education' : 'M.Com'
    }
}
print(users)
