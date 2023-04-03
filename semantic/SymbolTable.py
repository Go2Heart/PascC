import logging


# 注意Pascal大小写不敏感，所以在哈希表中，所有的标识符都转换为小写
# 注意不同作用域的名称可以相同
class HashTable(object):
    hash = {}  # 用字典代替哈希表

    # 以变量名为索引，值为符号表下标的列表(不可重复)

    @classmethod
    def insert(cls, name, index):  # 向哈希表中添加下标
        # 用列表模拟链式哈希表的链表
        name = name.lower()
        if cls.hash.get(name) is None:
            cls.hash[name] = [index]
        else:
            cls.hash[name].append(index)
            # 插入成功返回True，否则返回False

    @classmethod
    def find(cls, name):
        # 查询哈希表，获取变量名中对应的符号表下标的列表
        name = name.lower()
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
        name = name.lower()
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


class IndexStack():
    # Generate_flag = False
    cnt = 0
    stack = []
    # block_range = []  # [st,ed)是块号为i的块的符号表范围

    @classmethod
    def pushblock(cls):  # 索引栈入栈
        cls.stack.append(cls.cnt)
        # if not cls.Generate_flag:  # 当前是语义分析在调用
        #     cls.block_range.append([len(SymbolTable.table)])
        cls.cnt += 1

    @classmethod
    def popblock(cls):  # 索引栈出栈并返回栈顶
        ans = cls.stack.pop()
        # if not cls.Generate_flag:  # 当前是语义分析在调用
        #     cls.block_range[ans].append(len(SymbolTable.table))
        return ans

    @classmethod
    def topblock(cls):  # 返回索引栈栈顶，即当前块标识符
        return cls.stack[-1]


class SymbolTable():
    table = []  # 每一项为多元列表(块号，标识符名，类型，声明行，引用行列表)
    now_indexs = []  # 当前作用域内的符号表下标列表
    scan_index = 0  # 当前扫描到的符号表下标

    @classmethod
    def setIndexStack(cls):
        IndexStack.cnt = 0
        # IndexStack.Generate_flag = True

    # 通过块号+标识符名唯一定位一个多元列表
    @classmethod
    def print(cls):
        i = 0
        for item in cls.table:
            logging.debug('index = ' + str(i) + ' : ' + str(item))
            i += 1

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
            'name': name.lower(),
            'actual_name': name,
            'type': type,
            'declaration': declaration,
            'reference': reference
        })
        cls.now_indexs.append(len(cls.table) - 1)
        return True

    @classmethod
    def recover_const_var(cls):
        block = IndexStack.topblock()
        while cls.scan_index < len(cls.table) and \
              cls.table[cls.scan_index]['block'] == block and \
              cls.table[cls.scan_index]['type'].name != 'function':
            HashTable.insert(cls.table[cls.scan_index]['name'], cls.scan_index)
            cls.now_indexs.append(cls.scan_index)
            cls.scan_index += 1

    @classmethod
    def recover_function(cls):
        if cls.scan_index < len(cls.table):
            HashTable.insert(cls.table[cls.scan_index]['name'], cls.scan_index)
            cls.now_indexs.append(cls.scan_index)
            cls.scan_index += 1
            return True
        return False

    @classmethod
    def popblock(cls):  # 块结束时，重定位。索引栈出栈+更新符号表+更新哈希表
        block = IndexStack.popblock()
        while len(cls.now_indexs) > 0:
            item = cls.table[cls.now_indexs[-1]]
            if item['block'] == block:
                HashTable.delete(item['name'], item['block'])
                cls.now_indexs.pop()
            else:
                break

    @classmethod
    def pushblock(cls):  # 块开始时，定位。索引栈入栈+更新符号表
        IndexStack.pushblock()