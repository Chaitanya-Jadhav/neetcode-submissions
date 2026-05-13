class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # GLOBAL CHECK:
        # If the total gas available across all stations is less than the total 
        # cost to travel the entire circuit, it is mathematically impossible.
        if sum(gas) < sum(cost):
            return -1
        
        # 'total' tracks the current gas in our tank as we attempt the journey.
        total = 0
        
        # 'res' (result) tracks our current hypothesis for the starting station index.
        res = 0

        # Traverse through each gas station one by one.
        for i in range(len(gas)):
            # Update our tank with the net gas gained or lost at the current station.
            total += gas[i] - cost[i]

            # LOCAL CHECK:
            # If our tank drops below zero, it means our current starting station ('res') 
            # failed. We couldn't even reach station i + 1.
            if total < 0:
                # Because of the greedy property, if we can't reach station i+1 from 'res', 
                # we also can't reach it from ANY station between 'res' and 'i'.
                # Therefore, the earliest next possible starting point is i + 1.
                res = i + 1
                
                # Reset the tank to 0 for the new proposed starting point.
                total = 0
        
        # Because the global check at the top already guaranteed that a valid circuit 
        # exists, 'res' is guaranteed to be the correct, unique starting index.
        return res