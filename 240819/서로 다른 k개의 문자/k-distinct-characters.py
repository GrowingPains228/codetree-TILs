string, k = input().split()
k = int(k)
wordSet = set()
wordDict = dict()
string = ['#'] + list(string)
length = len(string)

j = 0
ans = 0
for i in range(1, length):
    while j + 1 < length:
        if string[j + 1] in wordSet or len(wordSet) + 1 <= k:
            wordDict[string[j + 1]] = wordDict.get(string[j + 1], 0) + 1
            wordSet.add(string[j + 1])
            j += 1
        else:
            break

    ans = max(ans, j - i + 1)

    wordDict[string[i]] -= 1
    if wordDict[string[i]] == 0:
        wordSet.remove(string[i])

print(ans)