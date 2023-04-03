# 91
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory)

# 92
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory["메로나"][0])

# 93
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory["메로나"][1])

# 94
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
inventory["월드콘"] = [500, 7]
print(inventory)

# 95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.keys())

# 96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(icecream.values())

# 97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

# 98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)  # + 로 추가 못함
print(icecream)

# 99
# zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)