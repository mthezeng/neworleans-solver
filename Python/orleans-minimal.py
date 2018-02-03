# Bite-sized version: one game, no error handling, minimal prints to screen.
def add_eight(class_size):
    assert class_size >= 2, 'Class size must be at least 2.'
    winning_pos, temp_class_size = 2, 2 # position 2 wins for a class size 2
    while temp_class_size < class_size:
        if winning_pos == 1:
            winning_pos += 7
            temp_class_size += 1
        else:
            winning_pos += 8
            temp_class_size += 1
        while winning_pos > temp_class_size:
            winning_pos -= temp_class_size
    return winning_pos

class_size = int(input('How many people will be playing today? '))
print('Position {0} will win.'.format(add_eight(class_size)))
