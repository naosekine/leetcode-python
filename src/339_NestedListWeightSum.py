from collections import deque
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        ans = []
        for ele in nestedList:
            s = 0
            nest = 1
            queue = deque()
            queue.append(ele)
            while queue:
                next_queue = deque()
                while queue:
                    e = queue.popleft()

                    if e.isInteger():
                        s += e.getInteger() * nest
                    else:
                        for i in e.getList():
                            next_queue.append(i)
                queue = next_queue
                nest += 1
                    
            ans.append(s)
        return sum(ans)