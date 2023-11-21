class opper :
    def __init__(self, codeName, score) :
        self.codeName = codeName
        self.score = score

member = 5

group = []
min_score = 101
min_idx = 0
for i in range(member) :
    codeName, score = tuple(input().split())
    score = int(score)
    if min_score > score :
        min_score = score
        min_idx = i

    group.append(opper(codeName, score))

min_opper = group[min_idx]
print(min_opper.codeName, min_opper.score)