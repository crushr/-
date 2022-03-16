# 利用二分递归进行快速排序

# 第一种是对空数组的append，好处是只用了一次for循环，需要定义两个新的数组。
# 第二种方法比第一种更方便，第二种的子数组分离是直接按条件切片，且是在一行上。
# 这里的递归的一大核心是数组拼接可以直接在return中用+号。

def fast_sort1(li):

    if len(li) <= 1:
        return li

    # //向上取整 %向下取整
    left  = []
    right = []

    # 确定基准值
    base = li[len(li) // 2]
    for item in li:
        if item < base:
            left.append(item)
        elif item > base:
            right.append(item)

    return fast_sort1(left) + [base] + fast_sort1(right)


def fast_sort2(li):
    if len(li) <= 1:
        return li
    
    base = li[0]
    less = [i for i in li[1:] if i <= base]
    more = [i for i in li[1:] if i > base]

    return fast_sort2(less) + [base] + fast_sort2(more)
 
print(fast_sort1([10,5,1,4,3,6]))
