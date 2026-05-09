class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers at the start and end of the array
        l, r = 0, len(nums) - 1

        # Continue searching as long as the search space is valid
        while l <= r:
            # Find the middle index to split the array into two halves
            mid = (l + r) // 2
            
            # Base case: we found the target
            if target == nums[mid]:
                return mid
            
            # Determine which half of the array is strictly sorted.
            # If the value at 'l' is less than or equal to the value at 'mid',
            # it guarantees the left half (from index l to mid) is perfectly sorted.
            if nums[l] <= nums[mid]:
                
                # Now check if the target falls OUTSIDE this sorted left half.
                # It's outside if it is larger than the maximum value in this half (nums[mid]),
                # OR smaller than the minimum value in this half (nums[l]).
                if target > nums[mid] or target < nums[l]:
                    # Since it's not in the left half, it must be in the right half.
                    # Move the left pointer to discard the left half.
                    l = mid + 1
                else:
                    # The target is within the bounds of the sorted left half.
                    # Move the right pointer to discard the right half.
                    r = mid - 1
            
            # If the left half is NOT sorted, then the rotation point is in the left half.
            # This means the right half (from mid to r) MUST be perfectly sorted.
            else:
                
                # Check if the target falls OUTSIDE this sorted right half.
                # It's outside if it is smaller than the minimum value in this half (nums[mid]),
                # OR larger than the maximum value in this half (nums[r]).
                if target < nums[mid] or target > nums[r]:
                    # Since it's not in the right half, it must be in the left half.
                    # Move the right pointer to discard the right half.
                    r = mid - 1
                else:
                    # The target is within the bounds of the sorted right half.
                    # Move the left pointer to discard the left half.
                    l = mid + 1
                    
        # If the loop finishes and we haven't returned 'mid', the target isn't in the array
        return -1