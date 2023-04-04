# 151
list = [3, -20, -3, 44]
for var in list:
    if var < 0:
        print(var)

# 152
list = [3, 100, 23, 44]
for var in list:
    if var % 3 == 0:
        print(var)

# 153
list = [13, 21, 12, 14, 30, 18]
for var in list:
    if var % 3 == 0 and var < 20:
        print(var)

# 154
list = ["I", "study", "python", "language", "!"]
for var in list:
    if len(var) >= 3:
        print(var)

# 155
list = ["A", "b", "c", "D"]
for var in list:
    if var == var.upper():  # var.isupper()
        print(var)

# 156
list = ["A", "b", "c", "D"]
for var in list:
    if var.islower():
        print(var)

# 157
list = ['dog', 'cat', 'parrot']
for var in list:
    #    print(var[0].upper()+var[1:])
    print(var.capitalize())

# 158
list = ['hello.py', 'ex01.py', 'intro.hwp']
for var in list:
    arr = var.split(".")
    print(arr[0])

# 159
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for var in list:
    arr = var.split(".")
    if arr[1] == "h":
        print(arr[0])

# 160
list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for var in list:
    arr = var.split(".")
    if arr[1] == "h" or arr[1] == "c":
        print(arr[0])