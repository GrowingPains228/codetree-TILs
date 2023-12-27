class Chat :
    def __init__(self, owner, unread_cnt) :
        self.owner, self.unread_cnt = owner, unread_cnt

n, m, p = tuple(map(int, input().split()))

chatting = []
for _ in range(m) :
    c,u = tuple(input().split())
    # 해당 메세지 기록
    chatting.append(Chat(c, int(u)))

People = [False] * n 
cur_person = ord(chatting[p-1].owner) - ord('A')
People[cur_person] = True
idx = p-1
while chatting[idx].unread_cnt == chatting[idx -1].unread_cnt :
    People[ord(chatting[idx-1].owner) - ord('A')] = True
    idx -= 1

ans = []
if chatting[p-1].unread_cnt > 0 :
    for i in range(p, m) :
        order = ord(chatting[i].owner) - ord('A')
        if People[order] :
            continue

        People[order] = True
else :
    for i in range(m) :
        if cur_person == i :
            continue

        People[i] = True

ans = [ chr(ord('A') + i) for i in range(n) if not People[i] ]

for elem in ans :
    print(elem, end = ' ')