class HashTable(object):
    hash = {}  # 用字典代替哈希表

    # 以变量名为索引，值为符号表下标的列表(不可重复)

    def insert(cls, name, index):  # 向哈希表中添加下标
        # 用列表模拟链式哈希表的链表
        if hash.get(name) is None:
            hash[name] = [index]
        else:
            if index in hash[name]:
                return False
                # 如果这个下标哈希表中已经有了，则不可插入
            else:
                hash[name].append(index)
                return True
            # 插入成功返回True，否则返回False

    def find(cls, name):
        # 查询哈希表，获取变量名中对应的符号表下标的列表
        ans = []
        for index in hash[name]:
            item = SymbolTable.table[index]
            if item['name'] == name:
                ans.append(index)
        return ans

    def delete(cls, name, block):
        # 删除哈希表中的某一块的某个标识符
        # 用列表模拟链式哈希表的链表
        if hash.get(name) is None:
            return False
        flag = False
        for index in hash[name]:
            item = SymbolTable.table[index]
            if item['name'] == name and item['block'] == block:
                hash[name].remove(index)  # 找到并成功删除
                flag = True
        if hash[name] == []:
            hash.pop(name)  # 如果链表为空，删除哈希表中的项
        return flag  # 删除成功返回True，否则返回False


class IndexStack(object):
    cnt = 0
    stack = []

    def pushblock(cls):  # 索引栈入栈
        cls.cnt += 1
        cls.stack.append(cls.cnt)

    def popblock(cls):  # 索引栈出栈并返回栈顶
        return cls.stack.pop()

    def topblock(cls):  # 返回索引栈栈顶，即当前块标识符
        return cls.stack[-1]


class SymbolTable(object):
    table = []  # 每一项为多元列表(块号，标识符名，类型，声明行，引用行列表)

    # 通过块号+标识符名唯一定位一个多元列表

    def getItem(cls, name):
        # 每次识别出标识符，当前块都要查询标识符
        # 从而处理重复声明、未声明
        indexs = HashTable.find(name)
        if len(indexs) == 0:
            return None
        return cls.table[max(indexs)]
        # 找不到返回None,否则返回基于最近控制域的符号表的具体项(字典)

    def insertItem(cls, name, type, declaration, reference):
        # 当前块要向符号表插入标识符
        item = cls.getItem(name)
        block = IndexStack.topblock()
        if item is not None and item['block'] == block:
            return False  # 发现当前块已经插入过这个标识符，拒绝插入
        if HashTable.insert(name, len(cls.table)):
            cls.table.append({
                'block': block,
                'name': name,
                'type': type,
                'declaration': declaration,
                'reference': reference
            })
            return True
        return False  # 哈希表中怎么会出现重复的符号表下标？说明出BUG了
        # 插入成功返回True，否则返回False

    def pushblock(cls):  # 块开始时，定位。索引栈入栈+更新符号表
        IndexStack.pushblock()

    def popblock(cls):  # 块结束时，重定位。索引栈出栈+更新符号表+更新哈希表
        block = IndexStack.popblock()
        while (cls.table[-1]['block'] == block):
            HashTable.delete(cls.table[-1].item['name'],
                             cls.table[-1].item['block'])
            cls.table.pop()
