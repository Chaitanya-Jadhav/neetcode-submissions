from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a frequency map to count occurrences of each number
        count = {}

        # Create a list of empty lists where index represents frequency
        # `freq[i]` will hold numbers that appear `i` times
        freq = [[] for i in range(len(nums) + 1)]

        # Step 2: Populate the frequency map
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 3: Bucket the numbers based on frequency
        for n, c in count.items():
            freq[c].append(n)

        res = []

        # Step 4: Traverse the frequency list in reverse (highest frequency first)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # Once we've collected k elements, return the result
                if len(res) == k:
                    return res
