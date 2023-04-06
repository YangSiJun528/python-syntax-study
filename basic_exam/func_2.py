# 211
def func(string):
    print(string)


func("안녕")
func("Hi")

print("안녕", "Hi")


# 212
def func(a, b):
    print(a + b)


func(3, 4)
func(7, 8)
print(7, 15)


# 213

#  함수에 맞는 인자를 입력하지 않으면 TypeError 발생

# 214

#  함수가 기대하는 타입를 입력하지 않아 TypeError 발생

# 215
def print_with_smile(string):
    print(string + ":D")


# 216

print_with_smile("안녕하세요")


# 217
def print_upper_price(a):
    print(a * 1.3)


print_upper_price(100)


# 218
def print_sum(a, b):
    print(a + b)


print_sum(10, 7)


# 219
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)


print_arithmetic_operation(10, 8)

# 220
def print_max(a, b, c):
    max = 0
    if a > max:
        max = a
    if b > max:
        max = b
    if c > max:
        max = c
    print(max)

print_max(11, 5, 7)