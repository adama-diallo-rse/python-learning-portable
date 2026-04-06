text = input("CamelCase: ")
result = ""

for char in text:
    if char.isupper():
        result += "_" + char.lower()
    else:
        result += char

print(result)