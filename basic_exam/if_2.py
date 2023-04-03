# 111
input1 = input("입력:")
print(input1 * 2)

# 112
input2 = input("숫자를 입력하세요:")
print(int(input2)+10)

# 113
input3 = int(input("숫자를 입력하세요:"))
print("짝수" if input3 % 2 == 0 else "홀수")

# 114
input4 = int(input("숫자를 입력하세요:"))
input4 += 20
print(255 if input4 >= 255 else input4)

# 115
input5 = int(input("숫자를 입력하세요:"))
input5 -= 20
if input5 > 255:
    rs = 255
elif input5 < 0:
    rs = 0
else:
    rs = input5
print(rs)

# 116
input6 = input("시간 입력:")
if input6[-2:] == "00":
    print("정각")
else:
    print("정각 아님")

# 117
fruit = ["사과", "포도", "홍시"]
input7 = input("좋아하는 과일은?:")
if input7 in fruit:
    print("정답")
else:
    print("오답")

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
input8 = input("투자 종목:")
if input8 in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input9 = input("좋아하는 계절:")
if input9 in fruit.keys():
    print("정답")
else:
    print("오답")

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input9 = input("좋아하는 과일:")
if input9 in fruit.values():
    print("정답")
else:
    print("오답")