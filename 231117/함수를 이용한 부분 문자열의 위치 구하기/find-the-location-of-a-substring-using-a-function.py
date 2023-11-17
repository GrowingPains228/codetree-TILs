string = input()
part = input()

def is_in_substring(substring) :
    for i in range(len(string) - len(substring) + 1) :
        for j in range(len(substring)) :
            if substring[j] != string[i + j] :
                break
        
            if j == len(substring)-1 :
                return i
            
    return -1


print(is_in_substring(part))