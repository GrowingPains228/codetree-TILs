A = input()
B = input()
leng_B = len(B)

while B in A :
    arr_A = list(A)

    # B가 존재하는 위치를 찾고
    index = A.index(B)

    # 위치에서 B의 길이만큼 제거 -> 여기서 index는 B의 처음 위치이므로
    for _ in range(leng_B) :
        arr_A.pop(index)
    
    A = ''.join(arr_A)

print(A)