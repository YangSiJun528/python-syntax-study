# 특징
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).

# 선언
a = set()
b = {1, 2, 3, 4}
c = set([1, 2, 3])
d = set("Hello")

print(a, b, c, d)
print(type(a), type(b), type(c), type(d))

# 집합 연산
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)  # 공집합
print(s1 | s2)  # 합집합
print(s1 - s2)  # 차집합
print(s1 ^ s2)  # 대칭차집합, 둘 중 한 집합에는 속하지만 둘 모두에는 속하지는 않는 원소들의 집합

# add, update, remove
s = set([1, 2, 3])
print(s)
s.add(5)
print(s)
s.update([1, 2, 3, 4])  # 여러 개의 값을 한꺼번에 추가 - 수정 X
print(s)
s.remove(4)
print(s)
