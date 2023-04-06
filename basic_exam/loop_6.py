# 181
list = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
print(list)

# 182
list = [["시가", "100", "200", "300"], ["종가", "80", "210", "330"]]
print(list)

# 183
stock = {"시가": ["100", "200", "300"], "종가": ["80", "210", "330"]}
print(stock)

# 184
stock = {"10/10": ["80", "110", "70", "90"], "10/11": ["210", "230", "190", "200"]}
print(stock)

# 185
apart = [[101, 102], [201, 202], [301, 302]]
for floor in apart:
    for i in floor:
        print(i, "호")

# 186
apart = [[101, 102], [201, 202], [301, 302]]
for floor in apart[::-1]:
    for i in floor:
        print(i, "호")

# 187
apart = [[101, 102], [201, 202], [301, 302]]
for floor in apart[::-1]:
    for i in floor[::-1]:
        print(i, "호")

# 188
apart = [[101, 102], [201, 202], [301, 302]]
for floor in apart:
    for i in floor:
        print(i, "호")
        print("-"*5)

# 189
apart = [[101, 102], [201, 202], [301, 302]]
for floor in apart:
    for i in floor:
        print(i, "호")
    print("-" * 5)

# 190
apart = [[101, 102], [201, 202], [301, 302]]
for floor in apart:
    for i in floor:
        print(i, "호")
print("-" * 5)
