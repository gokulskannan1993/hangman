from os import system, name
  
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
                   
                   
                   
                   '''


WORDS = ["ironman", "captainamerica", "spiderman", "hawkeye", "blackwidow", "doctorstrange", "antman", "thor", "loki","blackpanther","killmonger","ultron","thanos","starlord","drax","gamora","rocket","groot","mantis","yellowjacket","shuri","tonystark","mandarin","vulture","daredevil","captainmarvel","msmarvel","hulk","wasp","brucebanner","scottlang","pepperpotts","caroldanvers","peterparker","tchalla","mbaku","scarletwitch","wanda","vision","jarvis","edith", "auntmay", "happyhogan",]

won = '''


=========
YOU WON
=========

'''

lost = '''


=========
YOU LOST
=========

'''



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']