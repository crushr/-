#二分查找
def Binary_Search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (high + low) // 2

        if item == list[mid]:
            return mid
        if item < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None

List = [1,2,3,4,5,6,7,8]
Item = 5
print(Binary_Search(List,Item))
