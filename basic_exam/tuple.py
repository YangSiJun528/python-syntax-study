# 71
my_variable = ()
print(type(my_variable))

# 72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
movie_rank = "닥터 스트레인지", "스플릿", "럭키"  # 괄호( )를 생략해도 된다. 수정이 불가능 하기 때문에 새로운 튜플을 할당함
print(movie_rank, type(movie_rank))

# 73
one = (1,)  # 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다
print(one, type(one))

# 74
# 튜플은 불변이며, 순서가 있는 객체의 집합이다.
# 수정/삽입/삭제가 불가능하다.
# 따라서 수정 시 에러가 발생한다.

# 75
t = 1, 2, 3, 4
print(type(t))

# 76
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

# 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

# 79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c, ": apple banana cake")

# 80
# range(시작숫자, 종료숫자, step)
print(tuple(range(2,100,2))) # 2 <= n < 100 조건을 만족할 때까지 순차적으로 실행, 단 2번에 1번 씩