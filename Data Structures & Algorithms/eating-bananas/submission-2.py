class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We use Binary Search on the possible eating speeds (k).
        # Minimum possible speed is 1 banana/hour.
        # Maximum possible speed is max(piles) (eat largest pile in 1 hour).
        l, r = 1, max(piles)
        
        # This will store the minimum valid eating speed found.
        res = r

        # Standard Binary Search template
        while l <= r:
            # Mid represents a candidate eating speed (k bananas per hour)
            k = (l + r) // 2

            # Calculate total hours needed if Koko eats at speed k
            totalTime = 0
            for p in piles:
                # Time needed for each pile:
                # ceil(p / k) because she can't partially eat a pile in one hour
                totalTime += math.ceil(float(p) / k)
            
            # If total hours is within allowed hours,
            # this speed works → try to find a smaller valid speed
            if totalTime <= h:
                res = k          # Update result (valid speed found)
                r = k - 1        # Search left half (smaller speeds)
            else:
                # If total hours exceeds h,
                # speed is too slow → increase speed
                l = k + 1        # Search right half (larger speeds)

        # Return the minimum valid speed found
        return res

# Time & Space Complexity
# Time complexity: O(n∗log⁡m)
# Space complexity: O(1)
#
# Where n is the length of the input array pilespiles and m is the maximum number of bananas in a pile. 