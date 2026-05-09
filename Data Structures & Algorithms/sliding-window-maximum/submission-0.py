from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        # 'q' stores indices. We maintain it such that the values in nums 
        # corresponding to these indices are in decreasing order.
        q = deque()  
        l = r = 0

        while r < len(nums):
            # MONOTONIC STEP:
            # Before adding the current element (nums[r]), remove all smaller 
            # elements from the back of the queue. They can never be the 
            # maximum for the current or any future window.
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # BOUNDARY CHECK:
            # If the index at the front of the queue (the current max) 
            # has fallen out of the left side of our window, remove it.
            if l > q[0]:
                q.popleft()

            # WINDOW COMPLETION:
            # Once our right pointer has moved at least 'k' steps, 
            # we start recording the maximums (which is always at q[0]).
            if (r + 1) >= k:
                output.append(nums[q[0]])
                # Slide the left boundary forward
                l += 1
            
            # Expand the right boundary
            r += 1

        return output