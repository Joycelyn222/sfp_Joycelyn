import random

# 1. Ask the user for their name
name = input("What's your name, agent? ")

# 2. Create two lists: adjectives and animals
adjectives = ["Sneaky", "Fierce", "Swift", "Brave", "Silent", "Clever"]
animals = ["Otter", "Tiger", "Panther", "Fox", "Eagle", "Wolf"]

# 3. Randomly choose one adjective and one animal
random_adjective = random.choice(adjectives)
random_animal = random.choice(animals)

# 4. Combine them into a codename
codename = f"{random_adjective} {random_animal}"

# 5. Generate a random lucky number from 1 to 99
lucky_number = random.randint(1, 99)

# 6. Print the final message to the user
print(f"\n🕵️ Welcome, Agent {name}!")
print(f"Your codename is: {codename}")
print(f"Your lucky number is: {lucky_number}")
