class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if typed[j-1] != typed[j]:
                    return False
                else:
                    j += 1
        
        if j < len(typed):
            a = j-1
            for t in range(j, len(typed)):
                if typed[a] != typed[t]:
                    return False
        return i == len(name)
