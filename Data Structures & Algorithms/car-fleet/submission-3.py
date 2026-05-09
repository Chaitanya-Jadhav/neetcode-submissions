class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Combine position and speed into a list of pairs so they stay together when sorted.
        pair = [[p, s] for p, s in zip(position, speed)]
        
        # 2. The stack will store the time it takes for each distinct *fleet* to reach the target.
        stack = []

        # 3. Sort by position (ascending), then iterate backwards [::-1].
        # We evaluate cars starting closest to the target first, moving back to the furthest car.
        for p, s in sorted(pair)[::-1]:
            
            # Calculate how long it takes this specific car to reach the target on its own.
            # Time = Distance / Speed
            time = (target - p) / s
            stack.append(time)

            # 4. Check for a collision/fleet formation:
            # If there are at least 2 times in the stack...
            # And the current car (stack[-1]) takes LESS OR EQUAL time compared to the car ahead of it (stack[-2])...
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                
                # ...it means the current car caught up to the car ahead!
                # Since they now form a fleet and move at the speed of the slower lead car,
                # we pop the current car's faster time off the stack. 
                # The time of the lead car (stack[-2]) correctly represents the whole fleet.
                stack.pop()
        
        # 5. After checking all cars, the remaining times in the stack represent the distinct fleets.
        return len(stack)