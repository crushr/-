# 利用递归方法实现数组元素求和
# 分而治之思想
# 递归项写在return里这样才能循环，不然会造成问题

# 相当于递归加上li[0]，当前序列的第一个数字，迭代次数为数组长度

def Sum(li):
    if li == []:
        return 0
    else:
        return li[0] + Sum(li[1:])

list = [1,2,3,4,5]
print(Sum(list))