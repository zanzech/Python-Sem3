bot = {"name": "Titan", "battery": 82, "mode": "auto"}
print(bot)
print("name:", bot["name"])

bot["battery"] -= 5
bot["speed"] = 0.6
print(bot)
print("keys:", list(bot.keys()))
print("values:", list(bot.values()))

print(bot.get("heading"))
print(bot.get("heading", 0))

log = ["E2", "E7", "E2", "E1", "E7", "E2"]
freq = {}
for code in log:
    freq[code] = freq.get(code, 0) + 1
print("error freq:", freq)

# character frequency of name
name = "tapasay"
char_counts = {}
for ch in name:
    char_counts[ch] = char_counts.get(ch, 0) + 1

print("name:", name)
for letter in sorted(char_counts, key=char_counts.get, reverse=True):
    print(f"{letter} occurred {char_counts[letter]} times")

top = max(char_counts, key=char_counts.get)
print("most frequent letter:", top)
