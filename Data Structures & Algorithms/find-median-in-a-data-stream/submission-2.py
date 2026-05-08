class MedianFinder:

    def __init__(self):
        # 'small' is a max-heap that will store the smaller half of the numbers.
        # Note: Python's heapq only implements a min-heap. To simulate a max-heap, 
        # we store the numbers as negative values.
        self.small = []
        
        # 'large' is a min-heap that will store the larger half of the numbers.
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Add to 'small' heap by default.
        # We multiply by -1 to push the value into our simulated max-heap.
        heapq.heappush(self.small, -num)

        # Step 2: Maintain the order property.
        # Every number in 'small' must be <= every number in 'large'.
        # If the largest number in 'small' (at index 0) is greater than the 
        # smallest number in 'large' (at index 0), we have a violation.
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            # Fix it by popping the largest from 'small' and moving it to 'large'.
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Step 3: Maintain the size property (Balance the heaps).
        # The size difference between the two heaps cannot exceed 1.
        
        # If 'small' has over 1 more element than 'large', move the top element over.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # If 'large' has over 1 more element than 'small', move the top element over.
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If the total number of elements is odd, the median is the root of the larger heap.
        
        # If 'small' has more elements, return its largest element (remember to invert the sign).
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
            
        # If 'large' has more elements, return its smallest element.
        if len(self.large) > len(self.small):
            return self.large[0]
            
        # If the total number of elements is even, both heaps are exactly the same size.
        # The median is the average of the largest element in 'small' and the smallest in 'large'.
        return ((-1 * self.small[0]) + self.large[0]) / 2.0