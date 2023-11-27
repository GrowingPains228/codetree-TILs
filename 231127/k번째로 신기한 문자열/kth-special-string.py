n, k, T = tuple(input().split())
n,k = int(n), int(k)

string_arr = [
    input() for _ in range(n)
]

def is_starting_str(elem ,T) :
    for i in range(len(T)) :
        if elem[i] != T[i] :
            return False

    return True

#사전순으로 정렬
string_arr.sort()

cnt = k
for elem in string_arr :
    if is_starting_str(elem, T) :
        cnt -= 1

    if cnt == 0:
        print(elem)
        break