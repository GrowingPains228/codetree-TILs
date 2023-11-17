A = input()

def is_palindrome(string) :
    if string == string[::-1] :
        return True
    else : 
        return False
    
print("Yes" if is_palindrome(A) else "No")