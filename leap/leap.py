def leap_year(year):
    if year % 4 == 0:
        if year < 100:
            return True
        else:
            if year % 100 == 0:
                return True if year % 400 == 0 else False    
            else:
                return True
    else:
        return False