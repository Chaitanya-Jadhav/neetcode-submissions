class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Define the search space for the eating speed 'k' (bananas per hour).
        # The minimum possible speed is 1. 
        # The maximum useful speed is the size of the largest pile (eating faster than this doesn't save more time, since it takes at least 1 hour per pile).
        l, r = 1, max(piles)
        
        # Initialize our result with the maximum possible speed as a baseline.
        res = r

        # Perform a binary search to find the absolute minimum speed needed.
        while l <= r:
            # k represents our current "guess" for the eating speed.
            k = (l + r) // 2

            totalTime = 0
            # Calculate the total hours required to eat all piles at speed 'k'.
            for p in piles:
                # math.ceil is used because any fractional hour counts as a full hour.
                # E.g., if a pile has 5 bananas and speed is 3, it takes 2 hours (ceil(1.66...)).
                totalTime += math.ceil(float(p) / k)
            
            # Did we finish eating within the allowed hours 'h'?
            if totalTime <= h:
                # This speed works! Save it as our best answer so far.
                res = k
                # See if we can get away with eating even slower (search the left half).
                r = k - 1
            else:
                # We took too long. The speed 'k' is too slow.
                # We must increase our eating speed (search the right half).
                l = k + 1
                
        # Return the minimum eating speed found.
        return res