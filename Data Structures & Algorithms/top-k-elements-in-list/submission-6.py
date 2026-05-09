class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        # Dictionary to store {number: frequency}
        count = {} 
        
        # Step 2: Prepare buckets for frequencies
        # Create an array of empty lists where the INDEX represents the frequency.
        # We need len(nums) + 1 because the maximum possible frequency of a number 
        # is the length of the array itself (e.g., if all numbers are the same).
        freq = [[] for i in range(len(nums) + 1)]

        # Populate the dictionary with the counts of each number
        for num in nums:
            # .get(num, 0) returns the current count of 'num', or 0 if it doesn't exist yet
            count[num] = 1 + count.get(num, 0)

        # Step 3: Group numbers by their frequency
        for n, cnt in count.items():
            # Place the number 'n' into the bucket corresponding to its frequency 'cnt'
            freq[cnt].append(n)

        # Step 4: Gather the top k frequent elements
        res = []
        
        # Iterate through the buckets backwards (from highest frequency to lowest)
        # We start at len(freq) - 1 and stop before 0 (since 0 frequency means no elements)
        for i in range(len(freq) - 1, 0, -1):
            
            # Check the bucket at frequency 'i'. It may contain multiple numbers or be empty.
            for num in freq[i]:
                res.append(num) # Add the number to our result list
                
                # As soon as we've collected exactly 'k' numbers, we are done
                if len(res) == k:
                    return res