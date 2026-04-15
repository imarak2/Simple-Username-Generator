import random
words = ["Muga", "Aero", "Luxe", "Kairo", "Zeno", "Nyx", "Orion", "Echo", "Rune", "Sora",
    "Axel", "Nova", "Zephyr", "Draco", "Onyx", "Vega",
    "Mopped", "Bumfuzzle", "Taradiddle", "Degust", "Divagate", "Collywobbles",
    "Diddyblud", "Noctambulist", "Einstein", "Furuncle", "Lollygag",
    "Eucatastrophe", "Awesome", "Person", "Epstein", "Mr", "Gyatty"
]
secondwords = [
    "Master", "PDFFile", "Lover", "Peabody", "Sherman", "Luffy", "Lava", "Beast",
    "Mango", "Mustard", "Flavour", "Water", "You", "System", "Enjoyer", "Today",
    "Josh", "Made", "Game", "Couch", "Player"
]
numbers = random.randint(1, 3000)
RandomAhhUsername = str(random.choice(words)) + str(random.choice(secondwords)) + str(numbers)
if "67" in str(numbers) or "55" in str(numbers):
    print(f"Your username is so tuff!: {RandomAhhUsername}")
elif "67" not in str(numbers) or "55" not in str(numbers):
    print(f"Here is your randomly generated username: {RandomAhhUsername}")