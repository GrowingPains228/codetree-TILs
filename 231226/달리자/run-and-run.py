n = int(input())
before = [0] + list(map(int, input().split()))
after = [0] + list(map(int, input().split()))

tmp_arr = before[::]
ans = 0
for i in range(n, 0, -1) :
    if after[i] == tmp_arr[i] :
        continue

    moved_person = after[i] - tmp_arr[i]
    for j in range(i-1, 0, -1) :
        if moved_person == 0 :
            break

        count_person = tmp_arr[j] if moved_person >= tmp_arr[j] else moved_person
        tmp_arr[i] += count_person
        ans += count_person * (i - j)
        tmp_arr[j] -= count_person
        moved_person -= count_person

print(ans)