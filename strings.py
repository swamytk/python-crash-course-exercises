name = "the RISC-V architecture"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "KaruppuSwamy"
last_name = "Thangaraj"
full_name = f"{first_name} {last_name}"
print(full_name)
full_name = f"Full name is '{first_name.upper()} {last_name.title()}'"
print(full_name)

fruits_list = "Fruits List:\n\tApple\n\tBanana\n\tJack Fruit\n"
print(fruits_list)

# right side whitespace stripped
language = "python "
print(language)
whitespace_stripped = language.rstrip()
print(f"begin_{whitespace_stripped}_ends")
# left side whitespace stripped
language = " python"
whitespace_stripped = language.lstrip()
print(f"begin_{whitespace_stripped}_ends")
# both the sides whitespace stripped
language = " python "
whitespace_stripped = language.strip()
print(f"begin_{whitespace_stripped}_ends")

# All whitespaces (space here) stripped
language = " py tho n "
whitespace_stripped = language.replace(" ", "")
print(f"begin_{whitespace_stripped}_ends")

url = "https://www.reddit.com"
print(url.removeprefix('https://'))
myname = 'Swamy Dr.'
print(myname.removesuffix('Dr.'))
# All whitespaces (space here) stripped
language = " py tho n "
whitespace_stripped = language.replace(" ", "_space_")
print(f"begin_{whitespace_stripped}_ends")

import this
