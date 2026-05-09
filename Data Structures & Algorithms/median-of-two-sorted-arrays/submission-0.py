class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Assign to A and B for easier reference
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        
        # 'half' represents the number of elements we need in the left partition
        # For odd total length, the right partition will hold the extra element
        half = total // 2

        # OPTIMIZATION: Always run binary search on the SMALLER array.
        # This guarantees O(log(min(m, n))) time complexity and prevents
        # 'IndexError' when calculating 'j' for the larger array.
        if len(B) < len(A):
            A, B = B, A

        # Set up binary search pointers for array A
        # 'l' is the left bound, 'r' is the right bound
        l, r = 0, len(A) - 1
        
        while True:
            # 'i' is the pointer/partition index for array A
            i = (l + r) // 2
            
            # 'j' is the corresponding partition index for array B.
            # We subtract 2 because indices are 0-based. 
            # (i + 1) + (j + 1) must equal 'half', leading to j = half - i - 2
            j = half - i - 2

            # Determine the border values around the partitions in A and B.
            # If the partition is at the extreme edges, use infinity / -infinity
            # to ensure the boundary checks (<=) naturally pass.
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # VALID PARTITION CHECK:
            # Are all elements on the left <= all elements on the right?
            if Aleft <= Bright and Bleft <= Aright:
                
                # If total length is ODD, the median is the smallest element 
                # in the right partition (since right has the extra element).
                if total % 2:
                    return min(Aright, Bright)
                
                # If total length is EVEN, the median is the average of the 
                # largest element on the left and the smallest on the right.
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # If A's left element is too big, move A's partition to the left
            elif Aleft > Bright:
                r = i - 1
                
            # If B's left element is too big (meaning A's partition is too far left),
            # move A's partition to the right
            else:
                l = i + 1