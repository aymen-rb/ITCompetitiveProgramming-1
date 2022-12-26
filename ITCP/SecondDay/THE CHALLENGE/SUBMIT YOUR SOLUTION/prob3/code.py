year = int(input())

if year%4 == 0 and year%100 != 0 or year%400 == 0 :
    print("it is a nice leap year")
else:
    print("not leap")