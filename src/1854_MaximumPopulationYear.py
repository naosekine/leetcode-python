class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        datas = []
        for birth, death in logs:
            datas.append((birth, 1))
            datas.append((death, -1))

        datas.sort()

        max_population = max_year = 0
        population = 0
        for year, change in datas:
            population += change
            if population > max_population:
                max_population = population
                max_year = year

        return max_year
        
# self-help solution
#         fastyear = logs[0][0]
#         fastyear = min([min(log[0], fastyear) for log in logs])
#         lastyear = logs[0][1]
#         lastyear = max([max(log[1], lastyear) for log in logs])
#         ans = 0
#         curr = 0
#         for year in range(fastyear, lastyear+1):
#             count = 0
#             for log in logs:
#                 if log[0] <= year < log[1]:
#                     count += 1
#             if count > curr:
#                 ans = year
#                 curr = count
            
#         return ans