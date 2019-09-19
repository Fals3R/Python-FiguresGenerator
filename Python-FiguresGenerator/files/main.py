# Created by Fals3R

var_size = input("Enter figure size (1 or higher): ")

if var_size is None or not var_size.isdigit() or not int(var_size) > 1:
    print("Runtime exception: Size must be integer and higher than 1")
    input("")
    exit(0)

print("\n---------------------------------------\n")

for i in range(1, int(var_size)+1):
    print('*'*i)

print("\n---------------------------------------\n")

for i in reversed(range(1, int(var_size)+1)):
    print('*'*i)

print("\n---------------------------------------\n")

for i in range(1, int(var_size)+1):
    print(' '*(int(var_size)-i) + '*'*i)

print("\n---------------------------------------\n")

for i in reversed(range(1, int(var_size)+1)):
    print(' '*(int(var_size)-i) + '*'*i)

print("\n---------------------------------------\n")

for i in range(1, int(var_size)+1):
    print(' '*(int(var_size)-i) + '*'*((i-1)*2 + 1))

print("\n---------------------------------------\n")

for i in reversed(range(1, int(var_size)+1)):
    print(' '*(int(var_size)-i) + '*'*((i-1)*2 + 1))

print("\n---------------------------------------\n")

for i in range(1, int(var_size)+1):
    print('*'*(int(var_size)))

print("\n---------------------------------------\n")

for i in range(1, int((int(var_size)+1)/2)):
    print('*'*(int(var_size)))

print("\n---------------------------------------\n")