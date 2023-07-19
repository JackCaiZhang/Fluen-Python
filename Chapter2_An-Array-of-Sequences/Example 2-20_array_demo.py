from array import array
from random import random


if __name__ == '__main__':
    # 利用一个可迭代对象建立一个双精度浮点数组（类型码为‘d’），这里用的可迭代对象是一个生成器表达式
    floats = array('d', (random() for i in range(10**7)))

    print('floats[-1] ->', floats[-1])

    fp = open('floats.bin', 'wb')
    floats.tofile(fp)  # 把数组存入一个二进制文件里
    fp.close()

    floats2 = array('d')  # 新建一个双精度浮点空数组
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)  # 1000万个浮点数从二进制文件里读取出来
    fp.close()

    print('floats[-1] ->', floats[-1])
    print('floats2 == floats: ', floats2 == floats)
