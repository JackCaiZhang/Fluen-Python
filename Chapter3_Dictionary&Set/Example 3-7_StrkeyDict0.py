class StrkeyDict0(dict):  # 集成基类 dict

    def __missing__(self, key):
        if isinstance(key, str):  # 如果找不到的键本身就是字符串，则抛出keyError异常
            raise KeyError(key)
        return self[str(key)]  # 如果找不到的键不是字符串，则把它转换成字符串再进行比较

    def get(self, key, default=None):
        try:  # 将查找工作用self[key]的形式委托给 __getitem__ 方法，这样在查找失败之前，还能通过 __missing__ 再给某个键一个机会
            return self[key]
        except KeyError:
            return default  # 如果抛出keyError，则说明__missing__也失败了，于是返回default

    # 先按照传入键原本的值来查找，如果找不到，再用str()方法把键转换成字符串再查找一次
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
