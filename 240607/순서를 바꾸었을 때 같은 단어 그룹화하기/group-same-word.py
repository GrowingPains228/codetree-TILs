n = int(input())
arr = list()
cnt_arr = list()
dic_Group = list()
for _ in range(n):
    string = input()
    arr.append(string)
    cnt_arr.append(1)
    dic = dict()
    for i in range(len(string)):
        if string[i] in dic:
            dic[string[i]] += 1
        else :
            dic[string[i]] = 1
    
    dic_Group.append(dic)

for i in range(n):
    for j in range(i+1, n):
        if len(arr[i]) != len(arr[j]) :
            continue
        
        tf = True
        for key, value in dic_Group[i].items():
            if key not in dic_Group[j] or dic_Group[j][key] != value:
                tf = False
                break
            
        if tf:
            cnt_arr[i] += 1
        
print(max(cnt_arr))