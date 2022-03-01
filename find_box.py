# 找盒子 2种思路的伪代码

# 1、每次取出一个盒子查找；找到的是盒子放回盒子堆；再取出一个盒子查找；
# 2、检查盒子中的每样东西，找到的是盒子就继续打开，直到找到为止;

# 第二种思路就是典型的递归思想

def find_box_1(method):
    box_all = method.make_box()
    while box_all is not empty:
        box = grab_box()
        for item in box:
            if item == key:
                return key
            elif item == box:
                back_box_all()

def find_box_2():
    for item in box:
        if item == box:
            find_box_2()
        elif item == key:
            return key