# 141
list = [100, 200, 300]
for var in list:
    print(var+10)

# 142
list = ["김밥", "라면", "튀김"]
for var in list:
    print("오늘의 메뉴:"+var)

# 143
list = ["SK하이닉스", "삼성전자", "LG전자"]
for var in list:
    print(len(var))

# 144
list = ['dog', 'cat', 'parrot']
for var in list:
    print(var, len(var))

# 145
list = ['dog', 'cat', 'parrot']
for var in list:
    print(var[0])

# 146
list = [1, 2, 3]
for var in list:
    print("3 x " + str(var))

# 147
list = [1, 2, 3]
for var in list:
    print("3 x " + str(var) + " = " + str(var*3))

# 148
list = ["가", "나", "다", "라"]
arr = range(1, 4, 1)
for var in arr:
    print(list[var])

# 149
list = ["가", "나", "다", "라"]
arr = range(0, 4, 2)
for var in arr:
    print(list[var])

# 150
list = ["가", "나", "다", "라"]
for var in list[::-1]:
    print(var)