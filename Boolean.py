print(2 > 1) #1
print(2 < 1) #0
print(2 >= 1) #1
print(2 <= 2) #1
print(2 == 1) #0
print(2 != 1) #1

print( 2 > 1 and "Hello" == "Hello") # 1 & 1
print(not True) #0
print(not not True) #1

#True == 1
print(f"True is {int(True)}")

x = 3
print(x > 4 or not (x < 2 or x == 3))

print(type(3))
print(type(True))
print(type("True"))

def hello():
    print("Hello!")

print(type(hello))
print(type(print))
