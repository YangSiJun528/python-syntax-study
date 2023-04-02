# 31
a = "3"
b = "4"
print(a + b, "34")

# 32
print("Hi" * 3, "HiHiHi")

# 33
print('-' * 80)

# 34
t1 = 'python'
t2 = 'java'
print((t1 + " " + t2 + " ") * 4)

# 35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이 %d" % (name1, age1))
print("이름: %s 나이 %d" % (name2, age2))

# 36
print("이름: {} 나이 {}".format(name1, age1))

# 37
print(f"이름: {name1} 나이 {age1}")

# 38
count = "5,969,782,550"
print(int(count.replace(",","")))

# 39
part = "2020/03(E) (IFRS연결)"
print(part[:7])

# 40
data = "   삼성전자    "
print(data.split())