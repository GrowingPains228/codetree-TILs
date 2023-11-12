string_arr = input().split()

if len(string_arr[0]) > len(string_arr[1]) :
    print(string_arr[0], len(string_arr[0]))
elif len(string_arr[0]) < len(string_arr[1]) :
    print(string_arr[1], len(string_arr[1]))
else :
    print("same")