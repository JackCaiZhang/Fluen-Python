import array

if __name__ == '__main__':
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)  # 用含有5个短整型有符号整数的数组（类型码是‘h’）创建一个memoryview

    print('len(memv)-> ', len(memv))
    print('memv[0]-> ', memv[0])  # memv里的5个元素与数组元素一样

    memv_oct = memv.cast('B')  # 把memv里的内容转换成‘B’类型，即无符号字符
    print('memv_oct.tolist()-> ', memv_oct.tolist())  # 将memv_oct转换成列表形式查看

    memv_oct[5] = 4  # 把位于位置5的字节赋值为4
    print('numbers-> ', numbers)  # 由于上一步把占2个字节的整数的高位字节改成了4，所以这个有符号整数的值就变成了1024
