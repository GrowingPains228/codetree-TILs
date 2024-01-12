from collections import deque

dq = deque()

n = int(input())
for _ in range(n) :
    command = input()

    if command.startswith("push_back") :
        dq.append(command.split()[1])
    elif command.startswith("push_front") :
        dq.appendleft(command.split()[1])
    elif command == "pop_back" :
        print(dq.pop()) 
    elif command == "pop_front" :
        print(dq.popleft()) 
    elif command == "front" :
        print(dq[0])
    elif command == "back" :
        print(dq[-1])
    elif command == "size" :
        print(len(dq))
    else :
        print(1 if not dq else 0)