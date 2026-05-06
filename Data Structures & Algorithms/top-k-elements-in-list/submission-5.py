class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Map each number to its total count
        # Time: O(n) | Space: O(n)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # 2. Bucket Sort: Index represents frequency, value is a list of numbers
        # The max frequency any element can have is len(nums)
        # 
        freq = [[] for i in range(len(nums) + 1)]

        for n, cnt in count.items():
            freq[cnt].append(n)

        # 3. Iterate backwards from the highest frequency bucket to the lowest
        # This ensures we pick the "Top K" most frequent elements first
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Once we hit k elements, we are done
                if len(res) == k:
                    return res

# Time & Space Complexity
# Time complexity: O(n)
# Space complexity: O(n)
