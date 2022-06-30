class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        workers_distances = []        
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                workers_distances.append((distance,i,j))
        
        used = set()
        usedworkers = set()
        workers_distances.sort()
        # workers_distances.sort(key=lambda x: (-x[0], -x[1], -x[2]))
        ans = [0] * len(workers)
        for _, worker, bike in workers_distances:
            if bike not in used and worker not in usedworkers:
                ans[worker] = bike
                used.add(bike)
                usedworkers.add(worker)
            else:
                continue
        
        return ans
        