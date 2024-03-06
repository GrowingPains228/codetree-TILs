n = int(input())
Jenga_arr = [int(input()) for _ in range(n)]
s1, e1 = tuple(map(int, input().split()))
s2, e2 = tuple(map(int, input().split()))


def remove_PartRange_anc_Copy(s, e):
    global Jenga_arr
    temp_arr = []
    for i in range(len(Jenga_arr)) :
        if i >= s and i <= e :
            continue
        temp_arr.append(Jenga_arr[i])

    # 배열 복사
    Jenga_arr = []
    for i in range(len(temp_arr)):
        Jenga_arr.append(temp_arr[i])

remove_PartRange_anc_Copy(s1-1, e1-1)
remove_PartRange_anc_Copy(s2-1, e2-1)

print(len(Jenga_arr))
for elem in Jenga_arr :
    print(elem)