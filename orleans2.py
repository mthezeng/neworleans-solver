"""
orleans2.py

New Orleans Solver version 2.0 in python3
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
 @version 20171104
"""

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
        size_of_class = int(input('How many people will be playing today? '))
        while size_of_class <= 1:
                if size_of_class < 0:
                        print('ERROR: Cannot have negative class size')
                else:
                        print('ERROR: At least 2 students must be in class')

                size_of_class = int(input('How many people will be playing today? '))
        return size_of_class

def is_game_over(the_class):
        game_over = False
        if len(the_class) == 1:
                game_over = True
        return game_over

def next_out(the_class, current):
        # returns one plus the index of the next student to get out within the list the_class
        out = current
        for i in range(8):
                out = next_student(the_class, out)
        return out

def next_student(the_class, current):
        # returns one plus the index of the next student still in the game within the list the_class
        student = current
        if current < len(the_class):
                student = current + 1
        elif current == len(the_class):
                student = 1
        return student
        
def output_winner(the_winner, positions):
        print('Position {0} will win.'.format(the_winner))
        print('You must sit {0} position(s) to the right of the student who starts with the pumpkin to win.'.format(positions))
        print('(Assuming the pumpkin is passed to the right every time.)\n')
        print('Congratulations! You won a B.U.G. Award!!! :)')

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

print_intro()
play_again = True
while play_again:
        class_size = get_class_size()
        class_array = []
        for i in range(class_size):
                class_array.append(i + 1)
        current_student = 1 #one plus index of the student currently with pumpkin
        student_out = 0 #initialized to 0
        while not is_game_over(class_array):
                student_out = next_out(class_array, current_student)
                del class_array[student_out - 1]
                current_student = student_out - 1
        winner = class_array[0]
        positions_right = winner - 1
        output_winner(winner, positions_right)
        play_again = prompt_play_again()
print('Have a great day!')
