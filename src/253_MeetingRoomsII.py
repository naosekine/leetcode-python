import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        info = []
        for start, end in intervals:
            heapq.heappush(info, (start, 's'))
            heapq.heappush(info, (end, 'e'))
        
        count =0
        count_info = []
        while info:
            i = heapq.heappop(info)
            if i[1] == 's':
                count += 1
            else:
                count -= 1
            count_info.append(count)
        return max(count_info)        
        
        