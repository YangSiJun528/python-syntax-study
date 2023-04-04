# 121
input1 = input()
if input1.islower():
    print(input1.upper())
else:
    print(input1.lower())

# 122
input2 = int(input("score:"))
if 80 < input2 <= 100:
    print("A")
elif 60 < input2 <= 80:
    print("B")
elif 40 < input2 <= 60:
    print("C")
elif 20 < input2 <= 40:
    print("D")
else:
    print("E")

# 123
input3 = input()
arr = input3.split(" ")
if arr[1] == "달러":
    print("%0.2f 원" % (float(arr[0]) * 1167))
elif arr[1] == "엔":
    print("%0.2f 원" % (float(arr[0]) * 1.096))
elif arr[1] == "유로":
    print("%0.2f 원" % (float(arr[0]) * 1268))
else:
    print("%0.2f 원" % (float(arr[0]) * 171))

# 124
input4 = input()
input5 = input()
input6 = input()
print(max([input4, input5, input6]))

# 125
input7 = input("휴대전화 번호 입력:")
arr = input7.split("-")
if arr[0] == "011":
    print("SKT")
elif arr[0] == "016":
    print("KT")
elif arr[0] == "019":
    print("LGU")
else:
    print("알수없음")

# 126
input8 = input("우편번호:")
if 0 <= int(input8[2]) <= 2:
    print("강북구")
elif 3 <= int(input8[2]) <= 5:
    print("도봉구")
elif 6 <= int(input8[2]) <= 9:
    print("노원구")

# 127
input9 = input("주민등록번호:")
print("남자" if input9[0] == "3" or input9[0] == "1" else "여자")

# 128
input0 = input("주민등록번호:")
arr = input0.split("-")
print("서울입니다." if 0 <= int(arr[1][0:2]) <= 8 else "서울이 아닙니다")

# 129
input11 = input("주민등록번호:")
sum = int(input11[0]) * 2 + int(input11[1]) * 3 + int(input11[2]) * 4 + int(input11[3]) * 5 + int(input11[4]) * 6 + int(
    input11[5]) * 7 + \
      int(input11[7]) * 8 + int(input11[8]) * 9 + int(input11[9]) * 2 + int(input11[10]) * 3 + int(
    input11[11]) * 4 + int(input11[12]) * 5  # \ << 줄바꿈
# print(sum)
# print(sum%11)
rs = 11 - sum % 11
# print(rs)
if str(rs) == input11[-1]:
    print("유효한 주민등록번호입니다.")
else:
    print("유효한 주민등록번호가 아닙니다.")

# 130
import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
max_price = int(btc["max_price"])
min_price = int(btc["min_price"])
opening_price = int(btc["opening_price"])
gap = max_price - min_price
# print(gap, min_price, max_price)
# print(gap+opening_price, max_price)
# print(btc)
if gap + opening_price > max_price:
    print("상승장")
else:
    print("하락장")
