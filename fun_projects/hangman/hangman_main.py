import random, os, sys
from tkinter import *

path_to_words_file = os.path.join(os.path.dirname(sys.argv[0]), "words.txt")

with open(path_to_words_file) as words_file:
    all_words = words_file.read().split('\n')
using_words = [wrd for wrd in all_words if len(wrd) > 4]

class Hangman():

    def __init__(self):
        self.root = Tk()
        self.root.title("Hangman")
        self.root.geometry("300x400")
        self.create_ui()
        self.start_game()
        self.root.mainloop()
        

    def create_ui(self):
        #frames
        message_frame = Frame(self.root, bg='light pink', bd=5, height=130, width=500)
        message_frame.grid(row=0, column=0)
        play_frame = Frame(self.root, bg='light green', bd=5, height=130, width=500)
        play_frame.grid(row=1, column=0)
        board_frame = Frame(self.root, bg='light blue', bd=5, height=130, width=500)
        board_frame.grid(row=2, column=0)
        letters_frame = Frame(self.root, bg='khaki1', bd=5, height=130, width=500)
        letters_frame.grid(row=3, column=0)
        new_game_frame = Frame(self.root, bg='tomato2', bd=5, height=130, width=500)
        new_game_frame.grid(row=4, column=0)
        #message label
        self.messageLabel = StringVar()
        mainLabel = Label(message_frame, textvariable=self.messageLabel)
        mainLabel.grid()
        self.set_message("Let's play Hangman!")
        #entry label
        textLabel = Label(play_frame, text='Enter')
        textLabel.grid(row=0,column=0)
        #letter entered
        self.entry_text = StringVar()
        self.entry_obj = Entry(play_frame, bd=5, textvariable=self.entry_text)
        self.entry_obj.grid(row=0,column=1)
        #submit button
        self.submit_button = Button(play_frame, text ="Submit", command = self.check_letter)
        self.submit_button.grid(row=0, column=2)
        self.root.bind('<Return>', self.bind_return)
        #New Game button
        self.new_game_button = Button(new_game_frame, text ="New Game", command = self.start_game)
        self.new_game_button.grid(row=3, column=0)
        #display words in board frame
        self.boardMessage = StringVar()
        boardLabel = Label(board_frame, textvariable=self.boardMessage)
        boardLabel.grid()
        #*********display game info********
        #letters label name
        letterslabelname = Label(letters_frame, text='Letters Entered: ')
        letterslabelname.grid(row=0,column=0)
        #show letters
        self.letters_used = StringVar()
        used_letters = Label(letters_frame, textvariable=self.letters_used)
        used_letters.grid(row=0, column=1)
        #word length label name
        wordlengthlabelname = Label(letters_frame, text='Word Length: ')
        wordlengthlabelname.grid(row=1,column=0)
        #show word length
        self.word_length = StringVar()
        word_length_obj = Label(letters_frame, textvariable=self.word_length)
        word_length_obj.grid(row=1, column=1)
        #guessed left label name
        guesses_left_labelname = Label(letters_frame, text='Guesses Left: ')
        guesses_left_labelname.grid(row=2,column=0)
        #show guesses left
        self.guess_left_message = StringVar()
        guesses_left_obj = Label(letters_frame, textvariable=self.guess_left_message)
        guesses_left_obj.grid(row=2, column=1)

    def bind_return(self, event):
        self.check_letter()

    def get_letter(self):
        letter = self.entry_text.get().upper()
        self.clear_entry()
        return letter
        
    def clear_entry(self):
        self.value = self.entry_obj.get()
        self.entry_obj.delete(0, len(self.value) + 1)
        return self.value

    def set_message(self, message):
        self.messageLabel.set(message)

    def set_board(self, board):
        self.boardMessage.set(board)

    def set_used_letters(self, letters):
        self.letters_used.set(letters)

    def set_word_length(self, length):
        self.word_length.set(str(length))

    def set_guesses_left(self, guesses):
        self.guess_left_message.set(str(guesses))

    def start_game(self):
        word = random.choice(using_words)
        using_words.remove(word)
        #play round
        self.set_message('Start Guessing!')
        self.game_obj = Game(word)
        self.play_it()
        
    def play_it(self):
        self.round_end = False
        self.set_message('Start Guessing!')
        self.set_board(' '.join(self.game_obj.guessed_word))
        self.set_used_letters(self.game_obj.letters_tried)
        self.set_guesses_left(self.game_obj.guesses_left)
        self.set_word_length(len(self.game_obj.word))

    def check_letter(self):
        if self.round_end:
            self.set_message('Game Over. Please Start a new game.')
            return
        letter = self.get_letter().upper()
        self.clear_entry()
        isok = self.game_obj.is_letter_ok(letter)

        if isok.lower() == 'ok':
            if letter in self.game_obj.word:
                self.game_obj.when_letter_in_word(letter)
                self.set_board(' '.join(self.game_obj.guessed_word))
                self.set_used_letters(self.game_obj.letters_tried)
                iswon = self.game_obj.check_won()
                if iswon:
                    self.set_message('Congratulations! You Won!')
                    self.round_end = True
                    return
                else:
                    self.set_message('You Got One!')
            else:
                self.game_obj.when_no_letter_in_word(letter)
                self.set_used_letters(self.game_obj.letters_tried)
                self.set_guesses_left(self.game_obj.guesses_left)
                self.set_message('Nope. Sorry.')
                if self.game_obj.guesses_left == 0:
                    self.set_message('Sorry. You ran out of attempts. The word is ' + self.game_obj.word)
                    self.round_end = True
                    return
        else:
            self.set_message(isok)
            

class Game():

    def __init__(self, word):
        self.word = word.upper()
        self.guessed_word = ['-' for char in word]
        self.guesses_left = 11
        self.letters_tried = []

    def update_guessed_word(self, letter, pos):
        """:pos is a list: containing the indexes where the letter occurs"""
        for index in pos:
            self.guessed_word[index] = letter

    def check_won(self):
        if '-' not in self.guessed_word:
            return True
        return False

    def when_letter_in_word(self, letter):
        wlist = list(self.word)
        positions = []
        [positions.append(index) for index, let in enumerate(self.word) if let == letter]
        self.update_guessed_word(letter, positions)

    def when_no_letter_in_word(self, letter):
        self.guesses_left -= 1
        self.letters_tried.append(letter)

    def is_letter_ok(self, letter):
        if len(letter) != 1:
            return 'Enter ONE letter'
        elif letter in self.letters_tried:
            return 'You have already tried that. Try again.'
        else:
            return 'ok'


Hangman()


