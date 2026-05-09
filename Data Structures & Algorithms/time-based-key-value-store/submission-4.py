class TimeMap:

    def __init__(self):
        # Dictionary to store key-value pairs. 
        # Format: { "key": [ ["value1", timestamp1], ["value2", timestamp2] ] }
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None: 
        # If the key doesn't exist in our dictionary yet, initialize it with an empty list
        if key not in self.keyStore:
            self.keyStore[key] = []
            
        # Append the new [value, timestamp] pair.
        # Note: In this problem, 'set' calls are strictly increasing in time,
        # so appending guarantees the list remains perfectly sorted by timestamp.
        self.keyStore[key].append([value, timestamp])        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # Fetch the list of [value, timestamp] pairs for the key. 
        # Default to an empty list if the key doesn't exist.
        values = self.keyStore.get(key, [])
        
        # Set up left and right pointers for binary search
        l, r = 0, len(values) - 1

        # Perform binary search to find the largest timestamp <= the target timestamp
        while l <= r:
            m = (l + r) // 2
            
            # If the timestamp at mid is less than or equal to our target timestamp:
            if values[m][1] <= timestamp:
                # This is a valid candidate. Store the value.
                res = values[m][0]
                # Since we want the *largest* valid timestamp, we keep searching 
                # to the right to see if there's a closer match.
                l = m + 1
            else:
                # The timestamp at mid is strictly greater than our target, 
                # so it's invalid. We must search the left half.
                r = m - 1
                
        # Return the most recently stored valid value, or "" if nothing was valid
        return res