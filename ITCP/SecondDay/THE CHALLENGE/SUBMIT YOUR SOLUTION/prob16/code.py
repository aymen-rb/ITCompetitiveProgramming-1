
x = int(input("give me x:"))
nb = 0
y = abs(x)

while y // 10 != 0 :
    c = y%10
    nb = nb*10+c
    y= y // 10
if x<0:
    print(-(nb*10+y))
else:
    print(nb*10+y)

