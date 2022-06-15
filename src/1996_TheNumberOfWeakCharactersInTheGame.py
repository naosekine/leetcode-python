class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        ans = 0
        curr_max = 0
        for _, d in properties:
            if d < curr_max:
                ans += 1
            else:
                curr_max = d
        return ans


# self-help solution (TLE)
#         for attacki, defensei in properties:
#             for attackj, defensej in reverse:
#                 if attacki < attackj and defensei < defensej:
#                     print('strong: ', attacki, defensei)
#                     print('weak: ', attackj, defensej)
#                     ans.append((attacki, defensei))
#                     break
#         # print(ans)
#         return len(ans)