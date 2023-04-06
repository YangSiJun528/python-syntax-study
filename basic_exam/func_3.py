# 221
def print_reverse(string):
    print(string[::-1])


print_reverse("python")


# 222
def print_score(arr):
    print(sum(arr) / len(arr))


print_score([1, 2, 3])


# 223
def print_even(arr):
    for i in arr:
        if i % 2 == 0:
            print(i)


print_even([1, 3, 2, 10, 12, 11, 15])


# 224
def print_keys(dic):
    for i in dic.keys():
        print(i)


print_keys({"이름": "김말똥", "나이": 30, "성별": 0})

# 225
my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}


def print_value_by_key(dic, date):
    print(dic[date])


print_value_by_key(my_dict, "10/26")


# 226
def print_5xn(string):
    num = len(string) // 5
    if num / 5 == 0:
        num += 1
    for i in range(num):
        print(string[i * 5: i * 5 + 5])


print_5xn("아이엠어보이유알어걸")


# 227
def printmxn(string, n):
    num = len(string) // n
    if num / n == 0:
        num += 1
    for i in range(num + 1):
        print(string[i * n: i * n + n])


printmxn("아이엠어보이유알어걸", 3)


# 228

def calc_monthly_salary(annual_salary):
    print(int(annual_salary / 12))


calc_monthly_salary(12000000)


# 229

def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)


my_print(a=100, b=200)  # 가능은 한데, IDE에서 자동완성 안해줘서 굳이?

print("왼쪽: 100", "오른쪽: 200")

# 230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

print("왼쪽: 200", "오른쪽: 100")

