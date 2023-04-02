# 21
letters = 'python'
print(letters[0], letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[-4:])

# 23
string1 = "홀짝홀짝홀짝"
print(string1[::2])  # [start(이상):end(미만):step(Optional,기본 1)] - step이 음수인 경우 뒤에서부터 읽음, 24번 문제 참고

# 24
string2 = "PYTHON"
print(string2[::-1])

# 25
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 26
print(phone_number.replace("-", ""))

# 27
url = "http://sharebook.kr"
extension = url.split(".")
print(extension[-1])

# 28
lang = 'python'
# lang[0] = 'P' - 문자열은 immutable하다. 수정 시 에러 발생
# print(lang, "Python")

# 29
string3 = 'abcdfe2a354a32a'
print(string3.replace('a', 'A'))

# 30
string4 = 'abcd'
string4.replace('b', 'B')
print(string4, "abcd")
"""
String은 불변이다.
replace()를 사용하면 string4 원본 값 자체가 바뀌는 것이 아닌 새로운 문자열을 반한한다.
"""

