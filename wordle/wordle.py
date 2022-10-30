import os
import art
import random
from colorama import Fore, Back, Style, init
import time

class Wordle:
    init(autoreset=True)

    def __init__(self):
        self.word_list = self.create_word_list()
        self.word = self.get_random_word()
        self.word_length = len(self.word)
        self.NUM_OF_TRIES = 6
        self.guesses = []
    
    def create_word_list(self):
        with open('words.txt') as file:
            words = file.readlines()
            words = [word.strip().upper() for word in words]
        return words

    def start_game(self):
        self.game()

    def print_wordle(self):
        art.tprint('WORDLE', font='tarty1')
        print('\t\t', end='')
        art.tprint('By Filbert', font='smallcaps3')
        print('\n')

    def game(self):
        for _ in range(self.NUM_OF_TRIES):
            if self.word in self.guesses:
                break

            self.print_table()
            
            guess = self.get_guess()
            self.guesses.append(guess)
                
        self.print_table()

        color = Fore.GREEN if self.word in self.guesses else Fore.RED
        style = Style.BRIGHT
        print(style + color + f'The word was {self.word}!\n')
        
        art.tprint('Thank you for playing!')
        

    def get_guess(self):
        while True:
            guess = input('Guess: ').upper()

            if not len(guess) == self.word_length:
                print(Fore.RED + f'Guess must be {self.word_length} letters long!\n')
                continue
            elif not guess.isalpha():
                print(Fore.RED + 'Guess must only contain alphabetical letters!\n')
                continue
            elif guess not in self.word_list:
                print(Fore.RED + 'Not in the word list!\n')
                continue
            
            return guess


    def print_table(self):
        table = self.get_table()
        self.clear_console()
        self.print_wordle()
        print(table)

    def get_table(self):
        table = ''
        for guess in self.guesses:
            for i, c in enumerate(guess):
                if c in self.word and self.word[i] == c:
                    table += self.green_color(c)
                elif c in self.word:
                    table += self.yellow_color(c)
                else:
                    table += self.default_color(c)
                table += self.space()
            table += self.new_line()

        for _ in range(self.NUM_OF_TRIES - len(self.guesses)):
            for _ in range(self.word_length):
                table += self.default_color()
                table += self.space()
            table += self.new_line()

        return table

    def default_color(self, letter=' '):
        return Style.BRIGHT + Fore.WHITE + Back.WHITE + f' {letter} '
    
    def green_color(self, letter):
        return Style.BRIGHT + Fore.WHITE + Back.GREEN + f' {letter} '

    def yellow_color(self, letter):
        return Style.BRIGHT + Fore.WHITE + Back.YELLOW + f' {letter} '

    def space(self):
        return Style.RESET_ALL + '  '

    def new_line(self):
        return Style.RESET_ALL + '\n\n'

    def clear_console(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def get_random_word(self):
        return random.choice(self.word_list)

if __name__ == '__main__':
    wordle = Wordle()
    wordle.start_game()
