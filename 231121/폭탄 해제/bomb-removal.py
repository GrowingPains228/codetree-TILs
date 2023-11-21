class special_obj :
    def __init__(self, code, color, second) :
        self.code = code
        self.color = color
        self.second = second

code, color, second = tuple(input().split())
user = special_obj(code, color, int(second))

print(f"code : {user.code}")
print(f"color : {user.color}")
print(f"second : {user.second}")