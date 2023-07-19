from collections import deque

if __name__ == '__main__':
    dq = deque(range(10), maxlen=10)
    print(dq)

    # 队列的旋转操作接受一个参数n：当n大于0时，队列的最右边的n个元素会被移动到队列的左边；
    # 当n小于0时，最左边的n个元素会被移动到右边。
    dq.rotate(3)
    print(dq)
    dq.rotate(-4)
    print(dq)

    # 当试图对一个已满（len(d) == d.maxlen）的队列做头部添加操作的时候，其尾部的元素会被删除掉。
    dq.appendleft(-1)  # 从头部添加元素
    print(dq)
    dq.extend([11, 22, 33])  # 从尾部添加元素
    print(dq)
    dq.extendleft([10, 20, 30, 40])  # 把迭代器里的元素逐个添加到双向队列的左边，因此迭代器里的元素会逆序出现在队列中。
    print(dq)
