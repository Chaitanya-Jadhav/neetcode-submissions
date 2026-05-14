class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Find the last occurrence of each character.
        # We use a dictionary to map each character to its highest index in the string.
        # For example, if s = "ababcbacadefegdehijhklij", lastIndex['a'] will be 8.
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        # res will store the sizes of our partitions
        res = []
        
        # size keeps track of the length of the current partition
        # end keeps track of the furthest index we must reach to close the current partition
        size, end = 0, 0

        # Step 2: Iterate through the string to build the partitions
        for i, c in enumerate(s):
            size += 1 # Include the current character in the current partition
            
            # Update the 'end' of the current partition. 
            # If the current character appears later in the string, we MUST extend 
            # our partition to at least that index to keep all identical letters together.
            end = max(end, lastIndex[c])

            # If our current index 'i' has reached the 'end' boundary, 
            # it means all characters seen so far do not appear anywhere past this point.
            # We can safely close the current partition.
            if i == end:
                res.append(size) # Save the size of the completed partition
                size = 0         # Reset size to 0 for the next partition
        
        return res