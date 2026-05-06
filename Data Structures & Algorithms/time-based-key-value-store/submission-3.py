class TimeMap:

    def __init__(self):
        # Dictionary to store:
        # key -> list of [value, timestamp]
        # Each key can have multiple values stored at different timestamps.
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key does not exist, initialize it with an empty list.
        if key not in self.keyStore:
            self.keyStore[key] = []
        
        # Append the new [value, timestamp] pair.
        # We assume timestamps are strictly increasing for each key.
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # This will store the best valid value found.
        # If no valid timestamp exists, return empty string.
        res = ""
        
        # Retrieve the list of [value, timestamp] pairs.
        # If key does not exist, default to empty list.
        values = self.keyStore.get(key, [])
        
        # Initialize binary search pointers.
        l, r = 0, len(values) - 1

        # We are looking for the value with the largest timestamp
        # that is <= the given timestamp.
        while l <= r:
            m = (l + r) // 2  # Middle index
            
            if values[m][1] <= timestamp:
                # Current timestamp is valid (<= target).
                # It could be our answer, but there might be a later
                # timestamp on the right that is still valid.
                # So we store it as the best candidate so far.
                res = values[m][0]
                
                # Move right to search for a closer (larger) valid timestamp.
                l = m + 1
            else:
                # Current timestamp is too large.
                # Discard right half and search left.
                r = m - 1
        
        # After binary search completes,
        # res contains the latest valid value found.
        return res

# Time & Space Complexity
# Time complexity: O(1) for set()set() and O(log⁡n) for get().
# Space complexity: O(m∗n)
#
# Where n is the total number of values associated with a key and m is the total number of keys. 


