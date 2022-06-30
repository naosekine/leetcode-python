class RandomizedSet:

    def __init__(self):
        self.l = []
        self.l_dic = {}

    def insert(self, val: int) -> bool:
        # print(self.l, self.l_dic)
        if val in self.l_dic:
            return False
        self.l_dic[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        # print(self.l, self.l_dic)
        if val not in self.l_dic:
            return False
        remove_idx = self.l_dic[val]
        last_ele = self.l[-1]
        self.l[remove_idx] = last_ele
        self.l_dic[last_ele] = remove_idx
        self.l.pop()
        self.l_dic.pop(val)   
        return True

    def getRandom(self) -> int:
        # print(self.l, self.l_dic)
        return choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()