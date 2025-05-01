import random
import time

# Define characters from different times
characters = {
    "medieval": {
        "name": "Sir Cedric the Brave",
        "greetings": [
            "Hail, traveler! From whence do you come?",
            "The dragons sleep tonight, fear not!"
        ],
        "replies": [
            "Aye, that be true wisdom!",
            "Verily, thou art clever indeed.",
            "The kingdom shall remember this day."
        ]
    },
    "future": {
        "name": "yashwanth",
        "greetings": [
            "Greetings, human. This is the year 3050.",
            "You are now linked to the quantum mainframe."
        ],
        "replies": [
            "Processing... Your answer is 99% correct.",
            "Emotion detected: curiosity. Good!",
            "Upgrade complete. You're learning fast."
        ]
    },
    "1990s": {
        "name": "kishan",
        "greetings": [
            "Yo! Welcome to the 90s net-world!",
            "AOL is down again... classic."
        ],
        "replies": [
            "Totally rad, dude!",
            "That’s some next-level thinking.",
            "You're surfing the data wave!"
        ]
    }
}

# Welcome message
print("=== Time Travel Chatbot ===")
print("Talk to a character from another era!")

# Time period selection
print("\nChoose a time period:")
for era in characters:
    print(f"- {era.title()}")

choice = input("\nYour choice: ").lower()

if choice not in characters:
    print("Sorry, that time period isn't available yet!")
else:
    char = characters[choice]
    print(f"\nConnecting to {char['name']}...\n")
    time.sleep(1)
    print(random.choice(char["greetings"]))

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print(f"{char['name']}: Farewell, traveler!")
            break
        else:
            print(f"{char['name']}: {random.choice(char['replies'])}")