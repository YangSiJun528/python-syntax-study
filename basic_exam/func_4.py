# 231

#  함수 내부에서 선언한 변수는 외부에서 사용할 수 없다.

# 232

def make_url(string):
    return "www." + string + ".com"


print(make_url("naver"))


# 233

def make_list(string):
    rs = []
    for i in range(len(string)):
        rs.append(string[i])
    return rs


print(make_list("abcd"))


# 234

def pickup_even(arr):  # list(string)로도 똑같은 결과를 얻을 수 있다.
    rs = []
    for i in arr:
        if i % 2 == 0:
            rs.append(i)
    return rs


print(pickup_even([3, 4, 5, 6, 7, 8]))


# 235

def convert_int(string):
    return int(string.replace(",", ""))  # replace()는 사용한 문자열의 값을 바꾼다.


print(convert_int("1,234,567"))


# 236
def func(num):
    return num + 4


a = func(10)  # 14
b = func(a)  # 18
c = func(b)  # 22
print(c)

print(22)


# 237
def func(num):
    return num + 4


c = func(func(func(10)))
print(c)

print(22)


# 238
def func1(num):
    return num + 4


def func2(num):
    return num * 10


a = func1(10)  # 14
c = func2(a)  # 140

print(c, 140)


# 239

def func1(num):
    return num + 4


def func2(num):
    num = num + 2
    return func1(num)


c = func2(10)
print(c)
print((10 + 2) + 4)


# 240
def func0(num):
    return num * 2


def func1(num):
    return func0(num + 2)


def func2(num):
    num = num + 10
    return func1(num)


c = func2(2)
print(c)

print(((2 + 10) + 2) * 2)
