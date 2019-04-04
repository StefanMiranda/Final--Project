def partition(arr, low, high):
    i = (low -1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return (i+1)
            
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
lst = []
size = int(input("Enter size of the list: "))
for i in range(size):
    elements = int(input("Enter an element: "))
    lst.append(elements)
low = 0
high = len(lst) - 1
quick_sort(lst, low, high)
print(lst)