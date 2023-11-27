n = int(input())

arr = list(map(int, input().split()))
new_arr = [(i, elem) for i, elem in enumerate(arr)]

new_arr.sort(key = lambda x : (x[1], x[0]))
answer = [ 0 for _ in range(n)]

for i, (index, _) in enumerate(new_arr) :
    answer[index] = i + 1

for i in range(n) :
    print(answer[i], end = ' ')