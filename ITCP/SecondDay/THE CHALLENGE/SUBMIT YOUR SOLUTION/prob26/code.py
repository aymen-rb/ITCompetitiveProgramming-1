def func (a):
    for i in range(len(a)):
        max = len(a[0])
        if len(a[i]) > max:
            max = len(a[i])
    
    for i in range(max + len(a)):
        print("*",end='')
    print()
    for i in range(len(a)):
       
        print("*",a[i],"*")
    
        
    for i in range(max + max-1):
        
        print("*",end='')

    
a = ["AYOUB", "IS", "!BEST", "ITC", "BNADM"]

func(a)