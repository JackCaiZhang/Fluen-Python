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
                # 获取单词的出现情况列表，如果单词不存在，把单词和一个空列表放进映射，然后返回这个空列表，
                # 这样就能在不进行第二次查找的情况下更新列表了
                index.setdefault(word, []).append(location)
    # 以字母顺序打印出结果
    for word in sorted(index, key=str.upper):
        print(word, index[word])
