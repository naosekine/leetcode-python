class Solution:
    def isDecomposable(self, s: str) -> bool:
        # 2, 3の倍数
        # 3の倍数+2, 3の倍数
        
        not3flag = False
        not3len = 0
        tmp = s[0]
        last = s[0]
        for i in range(1,len(s)):
            print(tmp)
            if last == s[i]:
                tmp += s[i]
            else:
                if not not3flag and len(tmp) % 3 != 0:
                    not3flag = True
                    not3len = len(tmp)
                elif not3flag and len(tmp) % 3 != 0:
                    return False
                tmp = s[i]
            last = s[i]
        if not not3flag and len(tmp) % 3 != 0:
            not3flag = True
            not3len = len(tmp)
        elif not3flag and len(tmp) % 3 != 0:
            return False

        if (not3len-2) % 3 != 0:
            return False
        else:
            return True