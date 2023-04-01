# 기본
a = "this is string"
print(a)

# 줄바꿈 포함
b = """this is 
string"""
print(b)

# 이스케이프 \
c = "\'Hello World\' \nHello \tWorld"
print(c)

# 문자열 연산
print("\n\n문자열 연산\n" + "=" * 20)
# 합치기
print("Python" + "!!!")

# 곱하기(복제)
print("Python" * 2)

# 길이 구하기
print(len("python"))

# 인덱싱
print("\n\n문자열 인덱싱\n" + "=" * 20)

txt = "Life is too short, You need Python"
num = "0123456789012345678901234567890123"
ten = "0         1         2         3   "
print(txt + "\n" + ten + "\n" + num)

# 슬라이싱
print(txt[17], num[17])

print(txt[17:30], num[17:30])  # 17 <= a < 30  ; 30은 포함 X

print(txt[19:-7])  # txt[19] ~ txt[-8] 포함

# 변수에 할당
fst = txt[:19]
snd = txt[19:]

print(fst)
print(snd)
print(txt[:])

# 포메팅
print("\n\n문자열 포메팅\n" + "=" * 20)

print("I eat %d apples." % 3)
print("I eat %s apples." % "four")

print("I eat %d apples. so I was sick %d days." % (3, 5))

"""
%s : 문자열
%c : 문자 하나
%d : 정수
%f : 부동 소수
%o : 8진수
%x : 16진수
%% : % 자체, %d%% 같은 상황에 쓰이며, \% 는 불가능
"""

print("%10s" % "hi")  # 왼쪽에 10 공벡
print("%-10djun." % 1234)  # 오른쪽에 10 공백

print("%0.2f" % 3.1415926535897932384626433)  # 소수점 표현

# 관련 함수
print("\n\n문자열 관련 함수\n" + "=" * 20)

