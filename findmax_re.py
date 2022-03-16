# 递归求最大数字
# 网上拿的代码，后来发现并不是递归思想，只是循环遍历

def findmax(li):
    max = li[0]
    for item in li[1:]:
        if type(item) == list:
            max = findmax(item)
        elif max < item:
            max = item
    return max


list = [1,2,3,4,5]
print(findmax(list))