
   #二分查找 1
def Binary_Search(list, item):
    #定义查找的初始位和结束位，指向所查找的起始下标
    low = 0
    high = len(list) - 1
    #当初始位和结束位之间还有值时，继续循环
    while low <= high:
        #定义中间位，向下取整
        mid = (high + low) // 2
        #先确定是否取到，再进行向左向右搜索，这很关键，如果先向左向右搜索会有bug
        if item == list[mid]:
            return mid
        if item < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    #无值返回none
    return None

List = [1,2,3,4,5,6,7,8]
Item = 5
print(Binary_Search(List,Item))