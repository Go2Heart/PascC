import logging
class HashTable(object):
    hash = {}  # 用字典代替哈希表

    # 以变量名为索引，值为符号表下标的列表(不可重复)

    @classmethod
    def insert(cls, name, index):  # 向哈希表中添加下标
        # 用列表模拟链式哈希表的链表
        if cls.hash.get(name) is None:
            cls.hash[name] = [index]
        else:
            cls.hash[name].append(index)
            # 插入成功返回True，否则返回False

    @classmethod
    def find(cls, name):
        # 查询哈希表，获取变量名中对应的符号表下标的列表
        if cls.hash.get(name) is None:
            return []
        ans = []
        for index in cls.hash[name]:
            item = SymbolTable.table[index]
            if item['name'] == name:
                ans.append(index)
        return ans

    @classmethod
    def delete(cls, name, block):
        # 删除哈希表中的某一块的某个标识符
        # 用列表模拟链式哈希表的链表
        if cls.hash.get(name) is None:
            return False
        flag = False
        for index in cls.hash[name]:
            item = SymbolTable.table[index]
            if item['name'] == name and item['block'] == block:
                cls.hash[name].remove(index)  # 找到并成功删除
                flag = True
        if cls.hash[name] == []:
            cls.hash.pop(name)  # 如果链表为空，删除哈希表中的项
        return flag  # 删除成功返回True，否则返回False


class IndexStack(object):
    cnt = 0
    stack = []

    @classmethod
    def pushblock(cls):  # 索引栈入栈
        cls.cnt += 1
        cls.stack.append(cls.cnt)

    @classmethod
    def popblock(cls):  # 索引栈出栈并返回栈顶
        return cls.stack.pop()

    @classmethod
    def topblock(cls):  # 返回索引栈栈顶，即当前块标识符
        return cls.stack[-1]


class SymbolTable(object):
    table = []  # 每一项为多元列表(块号，标识符名，类型，声明行，引用行列表)

    # 通过块号+标识符名唯一定位一个多元列表
    @classmethod
    def print(cls):
        for item in cls.table:
            logging.debug(item)

    @classmethod
    def getItem(cls, name):
        # 每次识别出标识符，当前块都要查询标识符
        # 从而处理重复声明、未声明
        indexs = HashTable.find(name)
        if len(indexs) == 0:
            return None
        return cls.table[max(indexs)]
        # 找不到返回None,否则返回基于最近控制域的符号表的具体项(是个字典)

    @classmethod
    def haveItem(cls, name):
        # 当前块是否已经插入过这个标识符
        block = IndexStack.topblock()
        item = cls.getItem(name)
        if item is not None and item['block'] == block:
            return True
        return False

    @classmethod
    def insertItem(cls, name, type, declaration, reference):
        # 当前块要向符号表插入标识符（插入前得先查询haveItem)
        if cls.haveItem(name):
            return False
        block = IndexStack.topblock()
        HashTable.insert(name, len(cls.table))
        cls.table.append({
            'block': block,
            'name': name,
            'type': type,
            'declaration': declaration,
            'reference': reference
        })
        return True

    @classmethod
    def popblock(cls):  # 块结束时，重定位。索引栈出栈+更新符号表+更新哈希表
        block = IndexStack.popblock()
        while (len(cls.table) > 0 and cls.table[-1]['block'] == block):
            HashTable.delete(cls.table[-1]['name'],
                             cls.table[-1]['block'])
            cls.table.pop()

    @classmethod
    def pushblock(cls):  # 块开始时，定位。索引栈入栈+更新符号表
        IndexStack.pushblock()
