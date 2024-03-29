import sys
class Stack :
    def __init__(self) :
        self.items = []
    
    def push(self, item) :
        self.items.append(item)


    def empty(self) :
        return not self.items
    
    def size(self) :
        return len(self.items)
    
    def pop(self) :
        if self.empty() :
            raise Exception("Stack is empty")
        
        return self.items.pop()
    
    def top(self) :
        if self.empty() :
            raise Exception("Stack is empty")
        
        return self.items[-1]
    

string = input()
s = Stack()
Correct = True
for elem in string :
    if elem == "(" :
        s.push("(")
    else :
        if s.empty() :
            Correct = False
            break

        s.pop()

if Correct and s.empty():
    print("Yes")
else :
    print("No")