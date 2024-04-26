k,n = tuple(map(int, input().split()))
answer = []

def print_all():
    for elem in answer:
        print(elem, end=' ')
    print()


def Resursion(curr_num):
    if curr_num == n+1:
        print_all()
        return
    
    for i in range(1,k+1):
        answer.append(i)
        Resursion(curr_num+1)
        answer.pop()

Resursion(1)