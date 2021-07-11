import urllib.request


import random

game_over = False



# Generate a random word
WORDS = ["ironman", "captainamerica", "spiderman", "hawkeye", "blackwidow", "doctorstrange", "antman", "thor", "loki","blackpanther","killmonger","ultron","thanos","starlord","drax","gamora","rocket","groot","mantis","yellowjacket","shuri","tonystark","mandarin","vulture","daredevil","captainmarvel","msmarvel","hulk","wasp","brucebanner","scottlang","pepperpotts","caroldanvers","peterparker","tchalla","mbaku","scarletwitch","wanda","vision","jarvis","edith", "auntmay", "happyhogan",]

answer = random.choice(WORDS).upper()


# Create blank array
display = []
for letter in answer:
    display += "_"




while not game_over:
    # Ask for user input
    guess = input("Guess a letter: ").upper()





    for position in range(0, len(answer)):
        letter = answer[position]
        print(f"Current position is {letter} and guess is {guess}")
        if(guess == letter):
            display[position] = letter


    print(display)
    if "_" not in display:
        game_over = True
        print("Your win")


