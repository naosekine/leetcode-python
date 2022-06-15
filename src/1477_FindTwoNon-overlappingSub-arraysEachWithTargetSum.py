class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INF = len(arr) + 1
        best = INF
        best_i_arr = [INF] * len(arr)
        
        left = 0
        curr_sum = 0
        for right in range(len(arr)):
            print(best_i_arr)
            print(curr_sum)
            curr_sum += arr[right]
            
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                print(right, left)
                best = min(best, best_i_arr[left-1] + right - left + 1)
                best_i_arr[right] = min(best_i_arr[right-1], right - left + 1)
            else:
                best_i_arr[right] = best_i_arr[right-1]
                
        if best == INF:
            return -1
        else:
            return best