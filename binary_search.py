# 二分查找2
def binary_research(list, target):
    head = 0
    tail = len(list) - 1
    while tail >= head:
        mid = (head + tail) // 2
        num = list[mid] #注意这边列表的应引用方式是中括号[]
        if num == target:
            return mid
        if  num > target:
            tail = mid - 1
        else:
            head = mid +1
    return None

List = [1,2,3,4,5,6]
print(binary_research(List,6))