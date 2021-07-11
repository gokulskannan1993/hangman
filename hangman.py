import requests, random



# Generate a random word

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
answer = random.choice(WORDS)
