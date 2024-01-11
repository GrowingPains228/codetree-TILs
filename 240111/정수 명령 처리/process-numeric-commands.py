class Stack :
    def __init__(self) :
        self.items = []

    def empty(self) :
        return not self.items
    
    def size(self) :
        return len(self.items)
    
    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        if self.empty() :
            raise Exception("Stack is empty")
        
        return self.items.pop()
    
    def top(self) :
        if self.empty() :
            raise Exception("Stack is empty")
        
        return self.items[-1]
    
n = int(input())
stack = Stack()
for _ in range(n) :
    command = input()

    if command == "size" :
        print(stack.size())
    elif command == "empty" :
        print(int(stack.empty()))
    elif command == "pop" :
        print(stack.pop())
    elif command == "top" :
        print(stack.top())
    else :
        command = command.split()
        stack.push(int(command[1]))