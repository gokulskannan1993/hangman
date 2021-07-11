import requests, random



# Generate a random word
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()

answer = random.choice(WORDS).upper()


# Create blank array
display = []
for letter in answer:
    display += "_"




# Ask for user input
guess = input("Guess a letter: ").upper()



for position in range(0, len(answer)):
    letter = answer[position]
    if(guess == letter):
        display[position] = letter



