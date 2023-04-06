# 201
def print_coin():
    print("비트코인")


# 202
print_coin()

# 203
for i in range(0, 100):
    print_coin()


#    print(i)

# 204
def print_coins():
    for i in range(100):  # start 기본값은 0
        print("비트코인")


#        print(i)

# 205
#  파이썬은 인터프리터 언어이기 떄문에 사용할 함수가 위에서 정의되어야만 한다.

# 206
def message():
    print("A")
    print("B")


message()
print("C")
message()

print("A", "B", "C", "A", "B")

# 207
print("A")


def message():
    print("B")


print("C")
message()

print("A", "C", "B")

# 208
print("A")


def message1():
    print("B")


print("C")


def message2():
    print("D")


message1()
print("E")
message2()

print("A", "C", "B", "E", "D")

# 209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

print("B", "A")

# 210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

print(("B","C")*3, "A")

