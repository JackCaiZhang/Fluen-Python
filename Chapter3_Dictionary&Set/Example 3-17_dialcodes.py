if __name__ == '__main__':
    DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan')
    ]

    d1 = dict(DIAL_CODES)  # 数据元组的顺序是按照国家的人口排名来决定的
    print('d:', d1.keys())
    d2 = dict(sorted(DIAL_CODES))  # 数据元组的顺序是按照国家的电话区号来决定的
    print('d2:', d2.keys())
    d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))  # 数据元组的顺序是按照国家名字的英文拼写来决定的
    print('d3:', d3.keys())
    assert d1 == d2 == d3  # 三个字典都是相等的，因为它们所包含的数据是一样的
