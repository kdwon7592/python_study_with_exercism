def square_of_sum(number):
    square_sum = 0
    
    for i in range (0, number):
        square_sum += (i + 1)
    
    return square_sum ** 2       

def sum_of_squares(number):
    sum_square = 0
    
    for i in range (0, number):
        sum_square += (i + 1) ** 2
    
    return sum_square     


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
