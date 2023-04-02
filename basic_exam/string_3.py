# 41
r_ticker = "btc_krw"
print(r_ticker.upper())

# 42
u_ticker = "BTC_KRW"
print(u_ticker.lower())

# 43
a = "hello"
a = a.capitalize() # capitalize() 문자열의 첫 번째 문자를 대문자로 만듦

# 44
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 45
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx") or file_name.endswith("xls"))

# 46
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 47
a = "hello world"
print(a.split(" "))

# 48
ticker = "btc_krw"
print(ticker.split("_"))

# 49
date = "2020-05-01"
print(date.split("-"))

# 50
data = "039490     "
print(data.rsplit())