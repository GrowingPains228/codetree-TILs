# 두번째 해설 방법이 너무 좋아서 다시 풀어봤다.
n = int(input())
arr = list(map(int, input().split()))

# 출력할 index 리스트를 만들어준다.
indices = list()

# 첫번째 idx는 무조건 답이된다.
indices.append(0)

for i in range(1, n) :
    # indices 리스트에서 가장 마지막 요소가 최근 가장 큰 요소의 idx를 나타내므로, 해당 idx를 가져온다
    last_idx = indices[-1]

    # 가장 큰 idx의 수와 현재 idx를 비교한다.
    if arr[i] > arr[last_idx] :
        indices.append(i)

# 뒤에서부터 idx를 출력한다.
for idx in indices[::-1] :
    print(idx + 1, end = " ")