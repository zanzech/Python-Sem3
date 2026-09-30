visited = {(0, 0), (0, 1)}
visited.add((1, 1))
visited.add((0, 0))
print("visited:", visited)
print("count:", len(visited))
print("(1, 1) visited?", (1, 1) in visited)
print("(5, 5) visited?", (5, 5) in visited)

codes = ["E2", "E7", "E2", "E1", "E7"]
print("raw:", codes)
print("unique:", set(codes))
print("unique count:", len(set(codes)))

pos = (3.5, 8.2)
x, y = pos
print(f"x = {x}, y = {y}")
single = (5,)
print(single, type(single))

# grid walk: 8 coords with repeats, check (2, 2)
cells = set()
path = [(0, 0), (0, 1), (1, 1), (2, 2), (0, 1), (1, 1), (2, 2), (3, 2)]
for p in path:
    cells.add(p)

print("cells:", cells)
print("distinct visited:", len(cells))
print("(2, 2) in cells?", (2, 2) in cells)