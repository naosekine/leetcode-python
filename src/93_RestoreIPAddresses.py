class Solution:
    def restoreIpAddresses(self, s):

        def valid(segment):
            if segment[0] != '0':
                return int(segment) <= 255
            else:
                return len(segment) == 1
            
        def generateIP(index, dots, currIP):
            if dots == 4 and index == n:
                res.append(currIP[:-1])
                return
            if dots > 4:
                return
            
            for i in range(index, min(index+3, n)):
                segment = s[index:i+1]
                if valid(segment):
                    generateIP(i+1, dots + 1, currIP+segment+'.')

        n = len(s)
        res = []
        generateIP(0, 0, '')
        return res