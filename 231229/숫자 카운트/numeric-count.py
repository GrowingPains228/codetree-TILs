n = int(input())
arr = [
	tuple(map(int, input().split()))
	for _ in range(n)
]

cnt = 0
for i in range(1, 10):
	for j in range(1, 10) :
		if i == j :
			continue
		
		for k in range(1,10) :
			if i == k or j == k :
				continue

			successed = True
			for a, num_cnt1, num_cnt2 in arr :
				x = a // 100
				y = a // 10 % 10
				z = a % 10

				cnt1, cnt2 = 0,0

				if x == i :
					cnt1 += 1
				if y == j :
					cnt1 += 1
				if z == k :
					cnt1 += 1
				if x == j or x == k :
					cnt2 += 1
				if y == i or y == k :
					cnt2 += 1
				if z == i or z == j :
					cnt2 += 1
				
				if cnt1 != num_cnt1 or cnt2 != num_cnt2 :
					successed = False
					break
			if successed :
				cnt += 1

print(cnt)