from collections import Counter
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            print(five, ten)
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
        
        
        # changes = {5: 0, 10: 0, 20: 0}
        # for bill in bills:
        #     change = bill - 5
        #     if bill == 10:
        #         if change == 5:
        #             if changes[5] <= 0:
        #                 return False
        #             else:
        #                 changes[5] -= 1
        #                 changes[10] += 1
        #     elif bill == 20:
        #             if changes[5] <= 0:
        #                 return False
        #             else:
        #                 if changes[10] > 0 and changes[5] > 0:
        #                         changes[10] -= 1
        #                         changes[5] -= 1
        #                         changes[20] += 1
        #                 elif changes[10] <= 0:
        #                     if changes[5] >= 3:
        #                         changes[5] -= 3
        #                         changes[20] += 1
        #                     else:
        #                         return False
        #     else:
        #         changes[5] += 1
        # return True