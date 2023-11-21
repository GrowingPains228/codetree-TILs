n, k, T = tuple(input().split())
n = int(n)
k = int(k)

# a가 b로 시작하는지 확인하는 함수
def check_str(parent_str, child_str) :
    length = len(child_str)

    return parent_str[:length] == child_str

# 해설에서는 전부 받아오는것이 아니라, 입력과 동시에 str을 확인해서 append 한다.
words = []
for _ in range(n) :
    word = input()
    if check_str(word, T) :
        words.append(word)

words.sort()

print(words[k-1])