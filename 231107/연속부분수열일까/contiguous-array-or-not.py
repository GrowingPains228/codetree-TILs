n1, n2 = tuple(map(int, input().split()))
A_arr = list(map(int, input().split())) # n1 개의 수열
B_arr = list(map(int, input().split())) # n2 개의 수열

# Algorism
# - 연속 부분수열이 되려면 연속되게 요소들이 일치하여야함.
# 1. A를 순회하면서 B의 첫번째 요소와 일치하는 index를 찾는다.
# 2. 찾았으면 그 다음 index의 요소를 비교한다
# 3. 2. 번 과정을 B수열의 길이만큼 반복한다 
#    -범위 : (range(n2))
#    -시작점과 끝점 : start_index = index/ end_index = index + n2-1
# 4. 수열 B가 수열 A의 연속부분수열이라면 Yes, 아니라면 No를 출력
tf = False
for index in range(0,n1) :
    if A_arr[index] == B_arr[0] :
        #에러 처리
        #"A수열의 길이"보다 "현재 발견된 index로 부터 B 수열길이를 더한 것" 보다 크거나 같아야함
        if index + n2 > n1 :
            break

        for i in range(1, n2) : 
            if A_arr[index + i] != B_arr[i] :
                break
            
            # 끝까지 순회해서 모든 요소가 같다면, 연속부분 수열임
            if i == n2-1 :
                tf = True
    if tf :
        break

print("Yes" if tf else "No")