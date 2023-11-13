string = input()

cnt_ee = 0
cnt_eb = 0
index = 0

len_string = len(string)

for i in range(len_string - len('ee') + 1) :
    if string[i:i+len('ee')] == 'ee' :
        cnt_ee += 1
    elif string[i:i+len('eb')] == 'eb' :
        cnt_eb += 1
    else :
        continue

print(cnt_ee, cnt_eb)