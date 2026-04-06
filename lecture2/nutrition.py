def main():
    fruit = input("Item: ").lower()
    if fruit in fruits:
        print(f"{fruit.capitalize()}, raw: {fruits[fruit]} calories per edible portion")


fruits = {
    "apple": 52,
    "avocado": 160,
    "banana": 89,
    "cantaloupe": 34,
    "grapefruit": 26,
    "grapes": 67,
    "honeydew melon": 36,
    "kiwifruit": 61,
    "lemon": 17,
    "lime": 20,
    "nectarine": 44,
    "orange": 47,
    "peach": 38,
    "pear": 57,
    "pineapple": 42,
    "plums": 30,
    "strawberries": 32,
    "watermelon": 30,
}


main()