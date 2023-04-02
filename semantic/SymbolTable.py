class Item(object):
    def __init__(self, name, value):
        pass


class HashTable(object):
    hash = {}  # 用字典代替哈希表

    def insert(cls, block, name, index):
        # 用列表模拟链式哈希表的链表
        if hash.get(block, name) is None:
            hash[(block, name)] = [index]
        else:
            hash[(block, name)].append(index)

    def delete(cls, block, name):
        # 用列表模拟链式哈希表的链表
        for index in hash[(block, name)]:
            item = SymbolTable.table[index]
            if item['block'] == block and item['name'] == name:
                hash[(block, name)].remove(index)
        if hash[(block, name)] == []:
            hash.pop((block, name))

    def find(cls, block, name):
        ans = None
        for index in hash[(block, name)]:
            item = SymbolTable.table[index]
            if item['block'] == block and item['name'] == name:
                ans = index  # 遍历哈希表的链，获取符号对应的符号表下标
        return ans


class IndexStack(object):
    cnt = 0
    stack = []

    def pushblock(cls):  # 索引栈入栈
        cls.cnt += 1
        cls.stack.append(cls.cnt)

    def popblock(cls):  # 索引栈出栈
        return cls.stack.pop()


class SymbolTable(object):
    table = []  # 每一项为多元列表(块号，标识符名，类型，声明行，引用行列表)

    # 通过块号+标识符名唯一定位一个多元列表

    def getItem(cls, block, name):  # 通过块号和标识符名查找标识符
        index = HashTable.find(block, name)
        if index is None:
            return None
        return cls.table[index]

    def insertItem(cls, block, name):  # 插入标识符
        pass

    def pushblock(cls):  # 块开始时，定位。索引栈入栈+更新符号表
        IndexStack.pushblock()

    def popblock(cls):  # 块结束时，重定位。索引栈出栈+更新符号表
        now = IndexStack.pushblock()
