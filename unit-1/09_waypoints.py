errors = ["E2", "E7"]
print("errors:", errors)

errors.append("E9")
print("after append:", errors)

errors.insert(0, "E1")
print("after insert:", errors)

errors.remove("E7")
print("after remove:", errors)

a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(99)
print("a:", a)
print("b:", b)
print("c:", c)
print("b is a:", b is a, "| c is a:", c is a)

# filter list
readings = [10, -1, -1, 25, 30]
cleaned = [r for r in readings if r != -1]
print("cleaned:", cleaned)

nums = [12, 45, 7, 61, 33]
doubled = [x * 2 for x in nums]
big = [x for x in nums if x > 30]
print("doubled:", doubled)
print("big:", big)
