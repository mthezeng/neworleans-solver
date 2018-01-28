"""orleans3_investigation.py
This program prints cases where the winning position is 1 up to a user-inputted
class size, then finally prints the winning position of the user-inputted
class size.
"""

def get_class_size():
        size_of_class = int(input('How many people will be playing today? '))
        while size_of_class <= 1:
                if size_of_class < 0:
                        print('ERROR: Cannot have negative class size')
                else:
                        print('ERROR: At least 2 students must be in class')

                size_of_class = int(input('How many people will be playing today? '))
        return size_of_class

def output_winner(the_winner, positions):
        print('Position {0} will win.'.format(the_winner))

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

def add_eight(class_size):
    winning_pos = 2
    temp_class_size = 2
    if class_size == 2:
        winning_pos = 2
    else:
        while temp_class_size != class_size:
            if winning_pos == 1:
                print('Position {0} wins for a class size {1}'.format(winning_pos,temp_class_size))
                winning_pos = winning_pos + 7
                temp_class_size = temp_class_size + 1
            else:
                winning_pos = winning_pos + 8
                temp_class_size = temp_class_size + 1
            while winning_pos > temp_class_size:
                winning_pos = winning_pos - temp_class_size
    return winning_pos

play_again = True
while play_again:
        class_size = get_class_size()
        winner = add_eight(class_size)
        positions_right = winner - 1
        output_winner(winner, positions_right)
        play_again = prompt_play_again()
print('Have a great day!')
