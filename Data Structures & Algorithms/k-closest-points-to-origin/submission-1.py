class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize a list that will later be transformed into a min-heap
        minHeap = []

        # Iterate through each point to calculate its distance from the origin (0, 0)
        for x, y in points:
            # Calculate the squared Euclidean distance: (x2 - x1)^2 + (y2 - y1)^2.
            # Since the origin is (0,0), it simplifies to x^2 + y^2.
            # Note: We skip taking the square root because calculating roots is computationally 
            # expensive, and we only need to compare relative distances.
            dist = (x**2) + (y**2)
            
            # Append a list containing [distance, x, y].
            # Python's heapq sorts lists of lists based on the first element, 
            # so it will automatically prioritize the 'dist' value.
            minHeap.append([dist, x, y])
        
        # Transform the populated list into a valid min-heap in-place.
        # This specific operation is very efficient and takes O(N) time.
        heapq.heapify(minHeap)
        
        res = [] # List to store our final answer
        
        # We only need the 'k' closest points, so we loop 'k' times
        while k > 0:
            # heapq.heappop removes and returns the smallest item from the heap 
            # (which corresponds to the point with the shortest distance).
            dist, x, y = heapq.heappop(minHeap)
            
            # Add just the coordinates [x, y] to our result list
            res.append([x, y])
            
            # Decrement k since we just found one of the closest points
            k -= 1
        
        return res