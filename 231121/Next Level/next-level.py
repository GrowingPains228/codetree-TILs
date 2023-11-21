class character :
    def __init__(self, ID = "", LEVEL = 0) :
        self.ID = ID
        self.LEVEL = LEVEL
    
ch1 = character("codetree", 10)
ch2 = character()
ID, level = tuple(input().split())
ch2.ID, ch2.LEVEL = ID, level

print(f"user {ch1.ID} lv {ch1.LEVEL}")
print(f"user {ch2.ID} lv {ch2.LEVEL}")