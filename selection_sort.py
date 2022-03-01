# 选择排序
# 我的思路：遍历数组，找出其中值最大的元素索引，根据索引交换最大元素和首位元素的位置，接下来进行递归操作，每次首位元素向后顺移一位。

# 找出当前数组中最大的值的下标
def find_max_positon(list):
    position = 0   # 默认索引0
    max = list[0]  # 默认首位数值
    for i in range(1,len(list)):  # range(1,len(list))指第2个数到下标len(list)-1的数，即除第一个数之外的数
        if list[i] > max:
            max = list[i]
            position = i
    return position

# 找出当前数组中最小的值的下标
def find_min_positon(list):
    position = 0
    min = list[0]
    for i in range(1,len(list)): 
        if list[i] < min:
            min = list[i]
            position = i
    return position

# 交换list中两个元素位置 
def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# 遍历子数组，对子数组中最大值和首值进行交换 
def selection_sort(list):
    list1 = list2 = list
    for i in range(0,len(list)-1):
        list1 = swap(list1, i, find_max_positon(list1[i:])+i)  # 注意+i，取出的是子数组下标，交换时需要再加上i恢复原数组长度
        list2 = swap(list2, i, find_min_positon(list2[i:])+i)
    return list1,list2

List1 = [9,2,3,8,10,5] 
List2 = [-9,2,3,8,-10,5,0,-6] 
print(selection_sort(List2))


# 