a,b = tuple(map(int, input().split()))

def Is_AboutThree(number) :
    number = str(number)
    return number.find('3') != -1 or number.find('6') != -1  or number.find('9') != -1 
            
def count_threeNum(number) :
    return number%3 == 0

count = 0

for i in range(a, b+1) :
    if Is_AboutThree(i) or count_threeNum(i) :
        count += 1

print(count)