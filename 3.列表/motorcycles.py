# motorcycles.py 修改列表元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducat_i"
print(motorcycles)
# 添加元素
motorcycles.append("cat")
# 列表末尾添加元素
print(motorcycles)
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)
# 插入元素
motorcycles.insert(0, "ducat")
print(motorcycles)
# del删除元素 删除任何位置
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
# pop删除元素 删除最后一个元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
# 根据值删除元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.remove("suzuki")
print(motorcycles)
too_expensive = "honda"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA" + too_expensive.title()+" is too expensive for me.")

