from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
m_list = list(map(int, input().split()))
m_s = SortedSet()

for elem in m_list:
    m_s.add(elem)
    ans = 0
    length = len(m_s)
    
    ans = max(ans,  m_s[0] - 0)

    for i in range(1, length):
        ans = max(ans,  m_s[i] - m_s[i-1] - 1)

    ans = max(ans,  n - m_s[length-1])
    print(ans)