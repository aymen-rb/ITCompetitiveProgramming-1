def part(arr,min,max):
    pivot = arr[max]
    i = min - 1
    for j in range(min, max):
        if arr[j] <= pivot:
            i= i+1
            x= arr[j]
            arr[j]=arr[i]
            arr[i]= x
    x= arr[max]
    arr[max]=arr[i+1]
    arr[i+1]= x

    return i+1


def qs(arr,min,max):
    if min < max :
         k = part(arr,min,max)
         qs(arr, min, k - 1)
         qs(arr, k + 1, max)
    
         

t = [9,5,3,2]


qs(t,0,len(t)-1)
print(f'Sorted array: {t}')




        