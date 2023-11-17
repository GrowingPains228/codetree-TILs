A = input()

def find_alphaCount(string) :
    new_count_Arr = [
        0 for _ in range(ord('z') - ord('a') + 1)
    ]
    for elem in string :
        new_count_Arr[ord(elem) - ord('a')] += 1
    
    cnt = 0
    for i in range(ord('z') - ord('a') + 1) :
        if new_count_Arr[i] > 0 :
            cnt += 1
        
    return cnt > 2
    
print("Yes" if find_alphaCount(A) else "No")