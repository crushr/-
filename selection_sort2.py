# 找最小值的索引
def findsmallest_idx(arr):
    smallest = arr[0]
    smallest_idx = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx

# 排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # 找到最小值插入新数组
        smallest = findsmallest_idx(arr)
        newArr.append(arr.pop(smallest))  # smallest是索引
    return newArr

List2 = [-9,2,3,8,-10,5,0,-6] 
print(selectionSort(List2))