class Chat :
    def __init__(self, owner, unread_cnt) :
        self.owner, self.unread_cnt = owner, unread_cnt

n, m, p = tuple(map(int, input().split()))
humans = [ chr(i) for i in range(ord('A'), ord('A') + n+1) ]

chatting = []
for _ in range(m) :
    c,u = tuple(input().split())
    # 해당 메세지 기록
    chatting.append(Chat(c, int(u)))

People = [False] * n 
People[ord(chatting[p-1].owner) - ord('A')] = True

ans = []
if chatting[p-1].unread_cnt > 0 :
    for i in range(p+1, m) :
        order = ord(chatting[i].owner) - ord('A')
        if People[order] :
            continue

        People[order] = True

    ans = [
        chr(ord('A') + i) for i in range(n) if not People[i]
    ]

for elem in ans :
    print(elem, end = ' ')