s = input().rstrip()
p = input().rstrip()

len_s, len_p = len(s), len(p)

dp = [[False]*(len_p+1) for _ in range(len_s+1)]
s = " " + s
p = " " + p

dp[0][0] = True
for j in range(len_p):
    for i in range(len_s):
        if not dp[i][j] :
            continue
        
        # '*' 관련해서 판별하려면, 
        if j != len_p -1 and p[j+2] =='*':
            dp[i][j+2] = True

            for k in range(i+1, len_s + 1):
                if p[j+1] != '.' and s[k] != p[j+1]:
                    break
                dp[k][j+2] = True
        elif p[j+1] == '.':
            dp[i+1][j+1] = True
        else:
            if s[i+1] == p[j+1]:
                dp[i+1][j+1] = True

print("true" if dp[len_s][len_p] else "false")