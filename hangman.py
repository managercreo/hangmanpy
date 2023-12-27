import random
import os
import pyfiglet
from colorama import Fore
from colorama import Style



def run():

    you_win = pyfiglet.figlet_format("You Win! ")
    you_lose = pyfiglet.figlet_format("You Lose!")

    images = [f'''
  {Fore.RED}+---+
  |   |
      |
      |
      |
      |
=========''', f'''
  {Fore.RED}+---+
  |   |
  O   |
      |
      |
      |
=========''', f'''
 {Fore.RED} +---+
  |   |
  O   |
  |   |
      |
      |
=========''', f'''
 {Fore.RED} +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', f'''
 {Fore.RED} +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', f'''
 {Fore.RED} +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', f'''
 {Fore.RED} +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        'C',
        'Python',
        'JS',
        'Java',
        'PHP',
        'Ruby',
        'Perl'
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attempts = 6
    while True:
        os.system('clear')
        for char in spaces:
            print(char)
        print(images[attempts])
        letter = input(f"{Fore.CYAN}[+] Elige una letra: ").upper()
        
        found = False
        for idx, char in enumerate(word):
            if char.upper() == letter.upper():
                spaces[idx] = letter
                found = True


        if not found:
            attempts -= 1
            
        if "_" not in spaces:
            os.system('clear')
            print(f"{you_win}")
            print(f'{Fore.LIGHTCYAN_EX}[+] Ganaste con {attempts} intentos restantes! :D ')
            break

        if attempts == 0:
            os.system('clear')
            print(f"{you_lose}")
            print(f'{Fore.LIGHTRED_EX} [-] Perdiste y el pibe murio :(')
            print(f"La palabra era: {word}")
            break
        
        

if __name__ == '__main__':
    run()
