text = input("Input: ")
result = ""

for char in text:
    if char.lower() not in "aeiou":
        result += char

print(result)
    