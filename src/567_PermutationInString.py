class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dic = {}
        sub_s2_dic = {}
        for i in range(26):
            s1_dic[i] = 0
            sub_s2_dic[i] = 0
        
        for i in range(len(s1)):
            s1_dic[ord(s1[i]) - ord('a')] += 1
            sub_s2_dic[ord(s2[i]) - ord('a')] += 1

        start = 0
        end = len(s1) - 1
        
        while end < len(s2)-1:
            if s1_dic == sub_s2_dic:
                return True
            
            sub_s2_dic[ord(s2[start]) - ord('a')] -= 1
            start += 1
            end += 1
            sub_s2_dic[ord(s2[end]) - ord('a')] += 1
            
        if s1_dic == sub_s2_dic:
            return True
        else:
            return False