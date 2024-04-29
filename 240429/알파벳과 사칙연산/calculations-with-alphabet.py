string_arr = list(input())
string_length = len(string_arr)
string_mapper = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5
}
map_arr = [0]*6
ans = 0

def calculate():
    idx1 = string_mapper[string_arr[0]]
    result = map_arr[idx1]

    for i in range(1,string_length,2) :
        (op, str2) = string_arr[i], string_arr[i+1]
        idx = string_mapper[str2]
        target = map_arr[idx]
        result = operations(result, op, target)

    return result


def operations(result, op, target):
    if op == '+':
        return result + target
    elif op == '-':
        return result - target
    else:
        return result * target


def Recursion(num):
    global ans
    if num == 6:
        ans = max(ans, calculate())
        return

    for i in range(1,5):
        map_arr[num] = i
        Recursion(num+1)

Recursion(0)
print(ans)