# Tuple is an immutable list

# PC motherboard size standard in inches
micro_atx_mb = (9.6, 9.6)
mini_itx_mb = (5.9, 5.9)

# tuples can be redefined but no modifiable
my_mb = tuple(micro_atx_mb)
print(my_mb)
my_mb = (6, 7)
print(my_mb)

# Trying to modify, it should throw following error
# TypeError: 'tuple' object does not support item assignment
my_mb[1] = 5.6

