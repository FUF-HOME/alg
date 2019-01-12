class MyDictionary(object):
    def __init__(self):
        self.table_size = 13 
        self.key_list = [None] * self.table_size 
        self.value_list = [None] * self.table_size  

    def hashfuction(self, key):
        count_char = 0
        key_string = str(key)
        for key_char in key_string:  # 计算key所有字符的ASCII值的和
            count_char += ord(key_char)  # ord()函数用于求ASCII值
        length = len(str(count_char))
        if length > 3:  # 当和的位数大于3时，使用平方取中法，保留中间3位
            mid_int = (
                100 * int((str(count_char)[length // 2 - 1]))
                + 10 * int((str(count_char)[length // 2]))
                + 1 * int((str(count_char)[length // 2 + 1]))
            )
        else:  # 当和的位数小于等于3时，全部保留
            mid_int = count_char

        return mid_int % self.table_size  # 取余数作为散列值返回

    # 重新散列函数，返回新的散列值
    # hash_value为旧的散列值
    def rehash(self, hash_value):
        return (hash_value + 3) % self.table_size  # 向前间隔为3的线性探测

    def __setitem__(self, key, value):
        hash_value = self.hashfuction(key)
        if None == self.key_list[hash_value]:
            pass
        elif key == self.key_list[hash_value]:  # 哈希值处不为空，旧键值对与新键值对的key值相同，则作为更新，可以放置键值对
            pass
        else:  # 哈希值处不为空，key值也不同，即发生了“冲突”，则利用重新散列函数继续探测，直到找到空位
            hash_value = self.rehash(hash_value)  # 重新散列
            while (None != self.key_list[hash_value]) and (
                key != self.key_list[hash_value]
            ):  # 依然不能插入键值对，重新散列
                hash_value = self.rehash(hash_value)  # 重新散列
        # 放置键值对
        self.key_list[hash_value] = key
        self.value_list[hash_value] = value

    # 根据key取得value
    def __getitem__(self, key):
        hash_value = self.hashfuction(key)  # 计算哈希值
        first_hash = hash_value  # 记录最初的哈希值，作为重新散列探测的停止条件
        if None == self.key_list[hash_value]:  # 哈希值处为空位，则不存在该键值对
            return None
        elif key == self.key_list[hash_value]:  # 哈希值处不为空，key值与寻找中的key值相同，则返回相应的value值
            return self.value_list[hash_value]
        else:  # 哈希值处不为空，key值也不同，即发生了“冲突”，则利用重新散列函数继续探测，直到找到空位或相同的key值
            hash_value = self.rehash(hash_value)  # 重新散列
            while (None != self.key_list[hash_value]) and (
                key != self.key_list[hash_value]
            ):  # 依然没有找到，重新散列
                hash_value = self.rehash(hash_value)  # 重新散列
                if hash_value == first_hash:  # 哈希值探测重回起点，判断为无法找到了
                    return None
            # 结束了while循环，意味着找到了空位或相同的key值
            if None == self.key_list[hash_value]:  # 哈希值处为空位，则不存在该键值对
                return None
            else:  # 哈希值处不为空，key值与寻找中的key值相同，则返回相应的value值
                return self.value_list[hash_value]

    # 删除键值对
    def __delitem__(self, key):
        hash_value = self.hashfuction(key)  # 计算哈希值
        first_hash = hash_value  # 记录最初的哈希值，作为重新散列探测的停止条件
        if None == self.key_list[hash_value]:  # 哈希值处为空位，则不存在该键值对，无需删除
            return
        elif key == self.key_list[hash_value]:  # 哈希值处不为空，key值与寻找中的key值相同，则删除
            self.key_list[hash_value] = None
            self.value_list[hash_value] = None
            return
        else:  # 哈希值处不为空，key值也不同，即发生了“冲突”，则利用重新散列函数继续探测，直到找到空位或相同的key值
            hash_value = self.rehash(hash_value)  # 重新散列
            while (None != self.key_list[hash_value]) and (
                key != self.key_list[hash_value]
            ):  # 依然没有找到，重新散列
                hash_value = self.rehash(hash_value)  # 重新散列
                if hash_value == first_hash:  # 哈希值探测重回起点，判断为无法找到了
                    return
            # 结束了while循环，意味着找到了空位或相同的key值
            if None == self.key_list[hash_value]:  # 哈希值处为空位，则不存在该键值对
                return
            else:  # 哈希值处不为空，key值与寻找中的key值相同，则删除
                self.key_list[hash_value] = None
                self.value_list[hash_value] = None
                return

    # 返回字典的长度
    def __len__(self):
        count = 0
        for key in self.key_list:
            if key != None:
                count += 1
        return count


def main():
    H = MyDictionary()
    H["kcat"] = "cat"
    H["kdog"] = "dog"
    H["klion"] = "lion"
    H["ktiger"] = "tiger"
    H["kbird"] = "bird"
    H["kcow"] = "cow"
    H["kgoat"] = "goat"
    H["pig"] = "pig"
    H["chicken"] = "chicken"
    print("字典的长度为%d" % len(H))
    print("键 %s 的值为为 %s" % ("kcow", H["kcow"]))
    print("字典的长度为%d" % len(H))
    print("键 %s 的值为为 %s" % ("kmonkey", H["kmonkey"]))
    print("字典的长度为%d" % len(H))
    del H["klion"]
    print("字典的长度为%d" % len(H))
    print(H.key_list)
    print(H.value_list)


if __name__ == "__main__":
    main()
