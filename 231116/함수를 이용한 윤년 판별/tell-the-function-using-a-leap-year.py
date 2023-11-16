y = int(input())

def is_leapyear(date) :
    if date%4 == 0 and date % 100 == 0 and date % 400 == 0 :
        return True
    elif date%4 == 0 and date % 100 == 0 :
        return False
    elif date%4 == 0 :
        return True
    else : 
        return False


print("true" if is_leapyear(y) else "false")