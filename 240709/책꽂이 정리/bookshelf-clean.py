class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class BookCase:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    # 머리에 삽입
    def insert_head(self, book):
        if self.head is None:
            self.head = book
        else:
            self.head.prev = book
            book.next = self.head
            self.head = book

        if self.tail is None:
            self.tail = book
        
        self.count += 1

    def insert_head_books(self, a, b, cnt):
        if self.head is None:
            self.head = a
        else:
            b.next = self.head
            self.head.prev = b
            self.head = a

        if self.tail is None:
            self.tail = b

        self.count += cnt

    # 꼬리에 삽입
    def insert_tail(self, book):
        if self.tail is None:
            self.tail = book
        else:
            self.tail.next = book
            book.prev = self.tail
            self.tail = book
        
        if self.head is None:
            self.head = book

        self.count += 1    


    def insert_tail_books(self, a, b, cnt):
        if self.tail is None:
            self.tail = b
        else:
            a.prev = self.tail
            self.tail.next = a
            self.tail = b

        if self.head is None:
            self.head = a
        
        self.count += cnt


    def popLeft(self):
        if self.head is None:
            return None
        
        book = self.head
        self.count -= 1
        # 1개 밖에 없었던 경우
        if self.head.next is None:
            self.head = None
            self.tail = None
            return book

        # 여러개 있는 경우
        self.head = self.head.next
        self.head.prev = None
        book.next = None
    
        return book
    

    def popRight(self):
        if self.tail is None:
            return None

        book = self.tail
        self.count -= 1
        # 1개 밖에 없었던 경우
        if self.tail.prev is None:
            self.head = None
            self.tail = None
            return book

        # 여러개 있는 경우
        self.tail = self.tail.prev
        self.tail.next = None
        book.prev = None
        return book


    def popAll(self):
        if self.head is None:
            return (None, None, 0)

        (bookHead, bookTail) = self.head, self.tail
        cnt = self.count
        self.head = self.tail = None
        self.count = 0
        return (bookHead, bookTail, cnt)


    def printBooks(self):
        if self.head is None:
            print(0)
            return
        
        print(self.count, end = " ")

        book = self.head
        while book is not None:
            print(book.data, end = " ")
            book = book.next
        print()


n,k = tuple(map(int, input().split()))
bookCase = [BookCase() for i in range(k+1)]
books = [Node(i) for i in range(n+1)]

for i in range(1, n+1):
    bookCase[1].insert_tail(books[i])


# 해당 책꽂이의 맨 앞 책을 꺼낸다.
q = int(input())

for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        book = bookCase[cmd[1]].popLeft()
        if book is None:
            continue
        
        bookCase[cmd[2]].insert_tail(book)
    elif cmd[0] == 2:
        book = bookCase[cmd[1]].popRight()
        if book is None:
            continue
        
        bookCase[cmd[2]].insert_head(book)
    elif cmd[0] == 3:
        (startBook, endBook, cnt) = bookCase[cmd[1]].popAll()
        if startBook is None:
            continue
        
        bookCase[cmd[2]].insert_head_books(startBook, endBook, cnt)
    else:
        (startBook, endBook, cnt) = bookCase[cmd[1]].popAll()
        if startBook is None:
            continue
        
        bookCase[cmd[2]].insert_tail_books(startBook, endBook, cnt)

for i in range(1, k+1):
    bookCase[i].printBooks()