s = input().rstrip()
p = input().rstrip()

len_s, len_p = len(s), len(p)

dp = [False] * len(s)
cur_p_index = 0

for i in range(len_p):
    tf = False

    if cur_p_index >= len_s:
        break

    if p[i] == '*': # 당연히 처음부터 '*' 혼자 주어지지 않는다. 에러 가능성 없음.
        if 'a' <= p[i-1] <= 'z':
            while cur_p_index < len_s and s[cur_p_index] == p[i-1]:
                dp[cur_p_index] = True
                tf = True
                cur_p_index += 1
        else:
            while cur_p_index < len_s:
                dp[cur_p_index] = True
                tf = True
                cur_p_index += 1
    elif 'a' <= p[i] <= 'z' and s[cur_p_index] == p[i]:
            dp[cur_p_index] = True
            tf = True
            cur_p_index += 1
    else:
        dp[cur_p_index] = True
        tf = True
        cur_p_index += 1
    
    if not tf:
        break

print("true" if dp[len_s-1] else "false")