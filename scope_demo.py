# count=0
# def tick():
#     count=0
#     count+=1
#     return count
# print(tick(),tick(), count)

# threshold=70
# def is_alert(value):
#     thershold+=1
#     return value > threshold

# print(is_alert(85),is_alert(60))

# count=0
# def tick():
#     global count
#     count=count+1
#     return count

# print(tick())

# def t(count):
#     return count+1
# count=0
# count=t(count)
# count=t(count)
# print("COUNT",count)

def make_report():
    lines=["header"]
    lines.append("body")
    return len(lines)

print(make_report())
print(make_report())
print("lines" in dir())
