import collections
import re
import sys

if __name__ == '__main__':
    WORD_RE = re.compile(r'\w+')

    index = collections.defaultdict(list)  # 把list构造方法作为default_factory来创建一个defaultdict
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no)
                '''
                如果index中没有word的记录，那么default_factory会被调用，为查询不到的键创造一个值。
                这个值在这里就是一个空列表，然后这个空列表被赋值给index[word]，继而被当作返回值返回，
                因此，.append(location) 操作总能成功。
                '''
                index[word].append(location)

    # 以字母顺序打印出结果
    for word in sorted(index, key=str.upper):
        print(word, index[word])
