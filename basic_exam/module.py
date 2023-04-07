# 241
import datetime as dt
now = dt.datetime.now()
print(now)

# 242
now = dt.datetime.now()
print(now, type(now))

# 243
now = dt.datetime.now()
for i in range(5, 0, -1):
    day = dt.timedelta(i+1)
    print(now - day)

# 244
now = dt.datetime.now()
print(now.strftime("%H:%M:%S"))

# 245
day = dt.datetime.strptime("2020-05-04", "%Y-%m-%d")
print(day)

# 246
import time
for i in range(10):
    time.sleep(1)
    print(dt.datetime.now())

# 247

# 1. import os - os 모듈 전부 - 함수 호출 시 os.listdir() 식으로
# 2. from os import listdir - os 모듈의 listdir만 임포트 - listdir() 를 바로 호출 가능
# 3. from os import * - os 모듈 전부 - 함수 바로 호출 가능
# 4. ???

# 248
import os

print(os.getcwd())

# 249
os.rename(os.getcwd()+"/test/before.txt", os.getcwd()+"/test/before.txt")

# 250
import numpy as np
for i in np.arange(0, 5, 0.1): # arange() 는 실수 단위까지 표현할 수 있다.
    print(i)
