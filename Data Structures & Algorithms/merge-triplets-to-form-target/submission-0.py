class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 'good' is a set used to keep track of which target values (at index 0, 1, or 2) 
        # we have successfully found in valid triplets.
        good = set()

        # Iterate through every triplet in the given list
        for t in triplets:
            # FILTERING STEP:
            # If any value in the current triplet 't' is strictly GREATER than the 
            # corresponding value in our 'target', we cannot use this triplet. 
            # Why? Because merging uses the max() operation. If we include a triplet 
            # that overshoots the target, that position will forever remain larger 
            # than the target, making it impossible to win.
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue # Skip this triplet entirely
            
            # COLLECTION STEP:
            # If we reach here, it means the triplet is "valid" (no values exceed the target).
            # Now, we check each value in this valid triplet to see if it EXACTLY matches 
            # the corresponding target value.
            for i, v in enumerate(t):
                if v == target[i]:
                    # If it matches, add the index (0, 1, or 2) to our 'good' set.
                    # This means we found a valid piece of the puzzle for this position.
                    good.add(i)
        
        # FINAL CHECK:
        # If the length of our 'good' set is 3, it means we found valid triplets that 
        # perfectly hit the target value for position 0, position 1, and position 2.
        # Merging them will give us the exact target triplet.
        return len(good) == 3