# dimensions.py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 0 元组无法修改
for dimension in dimensions:
    print(dimension)
# 重新定义整个元组
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
