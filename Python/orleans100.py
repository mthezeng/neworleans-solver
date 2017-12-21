def is_game_over(the_class):
        """checks whether only one student is
        left in the game, and if so, returns true

        >>> arr = [0, 0, 3, 0, 0, 0]
        >>> is_game_over(arr)
        True
        """
        game_over = False
        students_left = 0
        for i in range(len(the_class)):
                if the_class[i] != 0:
                        students_left = students_left + 1
        if students_left == 1:
                game_over = True
        return game_over

def next_out(the_class, current):
        out = current
        i = 0
        while i < 8:
                out = next_student(the_class, out)
                i = i + 1
        return out

def next_student(the_class, current):
        """returns the next nonzero (i.e. still "in") student"""
        student = 0
        student_with_ball = current
        while student == 0:
                if student_with_ball < len(the_class):
                        student_with_ball = student_with_ball + 1
                        if the_class[student_with_ball - 1] != 0:
                                student = student_with_ball
                elif student_with_ball >= len(the_class):
                        student_with_ball = 1
                        if the_class[student_with_ball - 1] != 0:
                                student = student_with_ball
        return student

def find_winner(the_class):
        winner, i = 0, 0
        while winner == 0:
                if the_class[i] != 0:
                        winner = the_class[i]
                else:
                        i = i + 1
        return winner
        
def output_winner(the_winner, positions, class_size):
        print('Position {0} will win with a class size {1}.'.format(the_winner, class_size))

def main(index):
        class_size = index
        class_array = []
        for i in range(class_size):
                class_array.append(i + 1)
        current_student = 1
        student_out = 0
        while not is_game_over(class_array):
                student_out = next_out(class_array, current_student)
                class_array[student_out - 1] = 0
                current_student = student_out
        winner = find_winner(class_array)
        positions_right = winner - 1
        output_winner(winner, positions_right, class_size)

for i in range(3, 101):
	main(i)
print('Have a great day!')
