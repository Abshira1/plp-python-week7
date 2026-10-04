items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Numbered list
for i in range(len(items)):
    print(f"{i + 1}. {items[i]}")

# 2. Count names with more than 4 letters
count = 0
for item in items:
    if len(item) > 4:
        count += 1
print("Items with more than 4 letters:", count)

# 3. Longest name (manual comparison)
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item
print("Longest item:", longest)