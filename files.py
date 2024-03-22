from pathlib import Path

list = ['Swamy', 'Rajesh', 'Ganesh', "Muniyandi"]
name_file = Path('name_file.txt')
name_file.write_text(str(list))
content = name_file.read_text()
print(content)

lang_list = "Tamil Mother Tongue\nMalalyalam Sweet\nMarathi Rich\nEnglish Great\nHindi North\n"
lang_file = Path('lang_file.txt')
lang_file.write_text(lang_list)
content = lang_file.read_text()

# Handling lines
for line in content.splitlines():
    print(line)
    # Pattern matching
    if 'Sweet' in line:
        print("Sweet: pattern matching")    

# Handling words
words = content.split()
print(len(words))
for word in words:
    print(word)

# file exists or not check
path = Path("name_file_not_exists.txt")
if path.exists():
    print("File exists")
else:
    print("File not exists")


