# Bite-sized version: one game, no error handling, minimal prints to screen.
def add_eight(class_size):
    winning_pos = 2
    temp_class_size = 2
    if class_size == 2:
        winning_pos = 2
    else:
        while temp_class_size != class_size:
            if winning_pos == 1:
                winning_pos = winning_pos + 7
                temp_class_size = temp_class_size + 1
            else:
                winning_pos = winning_pos + 8
                temp_class_size = temp_class_size + 1
            while winning_pos > temp_class_size:
                winning_pos = winning_pos - temp_class_size
    return winning_pos

class_size = int(input('How many people will be playing today? ')) #must be >= 2
print('Position {0} will win.'.format(add_eight(class_size)))
