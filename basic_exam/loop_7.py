# 191
data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900]
]
for row in data:
    for col in row:
        print(col * 1.00014)

# 192
data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900]
]
for row in data:
    for col in row:
        print(col * 1.00014)
    print("-" * 4)

# 193
data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900]
]
rs = []
for row in data:
    for col in row:
        rs.append(col * 1.00014)
print(rs)

# 194
data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900]
]
rs = []
for row in data:
    temp = []
    for col in row:
        temp.append(col * 1.00014)
    rs.append(temp)
print(rs)

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
num = ohlc[0].index("close")
for row in ohlc[1:]:
    print(row[num])

# 196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
num = ohlc[0].index("close")
for row in ohlc[1:]:
    if row[num] > 150:
        print(row[num])

# 197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for row in ohlc[1:]:
    if row[3] >= row[0]:
        print(row[num])

# 198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for row in ohlc[1:]:
    volatility.append(abs(row[2]-row[1]))
print(volatility)

# 199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for row in ohlc[1:]:
    if row[3] > row[0]:
        volatility.append(abs(row[2]-row[1]))
print(volatility)

# 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
rs = 0
for row in ohlc[1:]:
    rs += row[0]-row[3]
#    print(row[0]-row[3])
print(rs)