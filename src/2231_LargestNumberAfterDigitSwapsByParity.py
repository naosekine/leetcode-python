class Solution:
    def largestInteger(self, num: int) -> int:
        k_g = []
        gusu = []
        kisu = []
        for i in str(num):
            if int(i) % 2 == 0:
                k_g.append(True)
                gusu.append(int(i))
            else:
                k_g.append(False)
                kisu.append(int(i))
                
        gusu.sort()
        kisu.sort()
        print(gusu, kisu, k_g)
        
        for i, x in enumerate(k_g):
            if x:
                n = gusu.pop()
                k_g[i] = str(n)
            else:
                n = kisu.pop()
                k_g[i] = str(n)
        print(k_g)
        return int(''.join(k_g))