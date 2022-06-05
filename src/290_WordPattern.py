class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lists = s.split()
        if len(lists) != len(pattern):
            return False
        dict_PS = {}
        for p, si in zip(pattern, lists):
            if p not in dict_PS:
                dict_PS[p] = si
            else:
                if dict_PS[p] != si:
                    return False
        if len(set(list(dict_PS.keys()))) != len(set(list(dict_PS.values()))):
            return False
        return True