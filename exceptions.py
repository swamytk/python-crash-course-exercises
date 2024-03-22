from pathlib import Path

file_to_read = Path('name_file_not_exists.txt')
# It throws a complete stack of code while throwing error
#content = file_to_read.read_text()
#print(content)

# exception handling
try:
    content = file_to_read.read_text()
except FileNotFoundError:
    # Exception message displayed to user
    #print("File Not Found")
    # Exception is silently ignored here
    pass
else:
    print("File read successfully!")


