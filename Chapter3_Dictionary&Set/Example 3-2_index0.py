import re
import sys

'''创建一个从单词到出现情况的映射'''
if __name__ == '__main__':
    WORD_RE = re.compile(r'\w+')

    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # 这其实是一种很不好的实现，这样写只是为了证明这个论点
                occurrences = index.get(word, [])  # 提取word出现的情况，如果还没有它的记录，则返回[]
                occurrences.append(location)  # 把单词新出现的位置添加到列表后面
                index[word] = occurrences  # 把新的列表放回字典中，这又牵扯到一次查询操作
    # 以字母顺序打印出结果
    # sorted函数的key=参数没有调用str.upper，而是把这个方法的引用传递给sorted函数
    for word in sorted(index, key=str.upper):
        print(word, index[word])
