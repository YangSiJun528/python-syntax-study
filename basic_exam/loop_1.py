# 131
fruit = ["사과", "귤", "수박"]
for var in fruit:
    print(var)
print(fruit[0], fruit[1], fruit[2])

# 132
fruit = ["사과", "귤", "수박"]
for var in fruit:
    print("#####")
print("#####", "#####", "#####")

# 133
for var in ["A", "B", "C"]:
    print(var)
print("A")
print("B")
print("C")

# 134
for var in ["A", "B", "C"]:
    print("변수:", var)
print("변수:", "A")
print("변수:", "B")
print("변수:", "C")

# 135
for var in ["A", "B", "C"]:
    print(var.lower())
print("a")
print("b")
print("c")

# 136
for var in [10, 20, 30]:
    print(var)

# 137
for var in [10, 20, 30]:
    print(var)

# 138
for var in [10, 20, 30]:
    print(var)
    print("-" * 7)

# 139
print("+" * 4)
for var in [10, 20, 30]:
    print(var)

# 140
for var in range(0, 4):  # range(start(이상), end(미만), step(기본 1))
    print("-" * 7)

# range
print(list(range(0, 5, 1)))
print(list(range(0, 10, 2)))
print(list(range(0, -5, -1)))
print(list(range(-10, -15, -1)))