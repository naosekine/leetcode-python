class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        press = ''
        last_bi = None
        for bi in s:
            if last_bi != bi:
                press += bi
            last_bi = bi
        return list(press).count('1') == 1