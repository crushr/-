# 利用递归方法实现数组元素求和
# 分而治之思想

def Sum(li):
    if li == []:
        return 0
    else:
        return li[0] + Sum(li[1:])

list = [1,2,3,4,5]
print(Sum(list))