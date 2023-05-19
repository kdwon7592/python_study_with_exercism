def steps(number):
    
    if(number < 1):
        raise ValueError("Only positive integers are allowed")
    
    step = 0
    
    while(number > 1): 
        #짝수이면
        if number % 2 == 0:
            number = number / 2
            step += 1
        else:
            number = number * 3 + 1
            step += 1
    
    return step