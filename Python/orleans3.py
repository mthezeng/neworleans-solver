"""
orleans3.py

New Orleans Solver version 3.0 in python3
 * DESCRIPTION:
 * This program will allow its user to solve the "Great Big House in New Orleans" game,
 * played by the students of Miss Jenny Bowman at Scottish Corners Elementary School.
 * The program will give the user the exact position at which they must sit in order to win.
 *
 * NOTE:
 * I realized an interesting detail while developing this program, which regards the initial
 * position of the "pumpkin". This program assumes that at the very start of the game, the
 * pumpkin is passed to the student at position 2. In other words, the student at position
 * 2 is the one who first sings "Great big...", and position 9 will be the first to get out
 * (if there are at least 9 students playing). In another version of the game, the person who
 * starts with the pumpkin will be the first to sing "Great big...", resulting in position 8
 * getting out first. That version is not simulated by this project.

 @author Michael Zeng
 @version 20171109
"""

import time
from sys import stdout

def print_intro():
	print('*****')
	print('Great Big House in New Orleans,')
	print('Forty stories hi-gh,')
	print('Every room that I\'ve been in,')
	print('Filled with pumpkin pi-e.')
	print('*****')
	print('Welcome! This program will tell you where you need to sit in order to win "Great Big House in New Orleans".')
	print('First, we\'ll need one piece of information from you.')
	print('*****')

def get_class_size():
    while True:
        try:
            size_of_class = int(input('How many people will be playing today? '))
            break
        except ValueError:
            print('ERROR: Class size must be an integer.')
    while size_of_class <= 1:
            if size_of_class < 0:
                    print('ERROR: Class size cannot be negative.')
            else:
                    print('ERROR: At least 2 students must be in class.')
            size_of_class = int(input('How many people will be playing today? '))
    return size_of_class

def output_winner(the_winner, start_time):
    elapsed = time.time() - start_time
    print('\nPosition {0} will win.'.format(the_winner))
    print('Congratulations! You won a B.U.G. Award!!! :)')
    print('Executed in {0} seconds.'.format(elapsed))

def prompt_play_again():
    play = False
    next_play = input('Would you like to play again? (y/n): ')
    while next_play != 'y' and next_play != 'n':
        print('Error detected. {0} not recognized.'.format(next_play))
        next_play = input('Would you like to play again? (y/n): ')
    if next_play == 'n':
        play = False
    elif next_play == 'y':
        play = True
        print('Playing again...')
        print('*****')
    return play

def prompt_progresstracker():
    print('An extremely large class size was detected.')
    print('The progress of the calculation can be tracked and displayed.')
    print('This can be useful for visualizing what the program is doing.')
    print('However, it significantly increases the time needed to obtain the result.')
    response = input('Would you like to track the progress of the calculation? (y/n): ')
    while response != 'y' and response != 'n':
        print('Error detected. {0} not recognized.'.format(response))
        response = input('Would you like to track the progress of the calculation? (y/n): ')
    if response == 'y':
        return True
    elif response == 'n':
        return False

def add_eight(class_size, progresstracker_needed):
    if class_size == 2:
        return 2
    else:
        winning_pos = 2
        temp_class_size = 2
        while temp_class_size < class_size:
            if winning_pos == 1:
                winning_pos += 7
                temp_class_size += 1
            else:
                winning_pos += 8
                temp_class_size += 1
            while winning_pos > temp_class_size:
                winning_pos -= temp_class_size
            if progresstracker_needed and temp_class_size % 1000000 == 0:
                if temp_class_size == 1000000:
                    print('Currently calculating class size 999999', end="")
                digits = len(str(temp_class_size - 1))
                delete = "\b" * (digits)
                print('{0}{1}'.format(delete, temp_class_size), end="")
                stdout.flush()
        return winning_pos

print_intro()
play_again = True
while play_again:
    class_size = get_class_size()
    progresstracker = False
    if class_size >= 5000000:
        progresstracker = prompt_progresstracker()
    t = time.time()
    winner = add_eight(class_size, progresstracker)
    output_winner(winner, t)
    play_again = prompt_play_again()
print('Have a great day!')
