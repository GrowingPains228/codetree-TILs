class Where_Dot :
    def __init__ (self, idx, value) :
        self.idx, self.value = idx, value

n = int(input())
arr = list(map(int, input().split()))
user_arr = [
    Where_Dot(i, value) for i, value in enumerate(arr)
]

user_arr.sort(key=lambda x : (x.value, x.idx))

order_arr = [
    0 for _ in range(n)
]

for i, elem in enumerate(user_arr) :
    order_arr[elem.idx] = i+1

for i in order_arr :
    print(i, end = " ")