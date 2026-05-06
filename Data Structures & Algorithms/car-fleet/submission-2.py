class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into pairs
        # Each element: [position, speed]
        pair = [[p, s] for p, s in zip(position, speed)]
        
        # This stack will store the time needed for each fleet
        # to reach the target
        stack = []

        # Sort cars by position in ascending order,
        # then iterate from the car closest to target
        # to the car farthest from target
        for p, s in sorted(pair)[::-1]:
            
            # Calculate time required for current car
            # to reach the target
            time = (target - p) / s
            
            # Push this car's time onto stack
            stack.append(time)

            # If the current car arrives earlier or at the same time
            # as the fleet in front of it, it joins that fleet
            # (because it catches up before reaching target)
            # So we remove it as a separate fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # The number of fleets is the size of the stack
        return len(stack)

# Time & Space Complexity
# Time complexity: O(nlog⁡n)
# Space complexity: O(n)
