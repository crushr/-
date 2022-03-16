# 递归求元素个数
# 和递归求元素和类似，不过是把len

# 相当于递归加上1，迭代次数为数组长度

def numlen(li):
    if len(li) == 0:
        return 0
    else:
        return 1 + numlen(li[1:])

list = [1,2,3,4,5]
print(numlen(list))