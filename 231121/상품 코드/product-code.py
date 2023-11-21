class Object : 
    def __init__(self, name = "", code = 0) :
        self.name = name
        self.code = code

product1 = Object("codetree", 50)
name, code = tuple(input().split())

product2 = Object(name, int(code))

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")