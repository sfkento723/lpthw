def bread_and_butter(breads, butters):
    print(f"You have {breads} loaves of bread and {butters} sticks of butter.")
    print(f"You know what they say! All toasters toast toast!")

print("Give function numbers directly:")
bread_and_butter(10, 20)

print("Use script variables:")
amount_of_bread = 30
amount_of_butter = 40
bread_and_butter(amount_of_bread, amount_of_butter)

print("Use math inside arguments:")
bread_and_butter(10 + 10, 20 + 20)

print("Use variables and math:")
bread_and_butter(amount_of_bread + 100, amount_of_butter + 100)
