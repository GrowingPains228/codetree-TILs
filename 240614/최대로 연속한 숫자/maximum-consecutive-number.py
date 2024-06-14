from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
m_list = list(map(int, input().split()))
m_s = SortedSet()
s_len = SortedSet()

# 시간 복잡도가 mlogm 으로 맞춰야 한다.
# 일단 m을 돌면서 최장 길이를 찾아줘야한다.
# 그래서 무조건 m의 시간복잡도는 보장이 되는거고,
# 이때, 
m_s.add(-1)
m_s.add(n+1)
s_len.add((-(n+1), -1, n+1))
for elem in m_list:
    m_s.add(elem)

    end = m_s[m_s.bisect_right(elem)]
    start = m_s[m_s.bisect_left(elem)-1]
    # 왼쪽, 오른쪽을 확인해서, 길이 체크
    # 오른쪽
    s_len.remove((-(end-start-1), start, end))
    s_len.add((-(elem - start -1), start, elem))
    s_len.add((-(end - elem - 1), elem, end))

    length, _, _ = s_len[0]
    print(-length)