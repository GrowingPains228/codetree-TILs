n = int(input())

new_arr = input().split()
new_arr = "".join(new_arr)

for i in range(0,len(new_arr),5) :
    print(new_arr[i:i+5])