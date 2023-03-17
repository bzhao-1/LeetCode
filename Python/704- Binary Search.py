class Solution:
    #Violates principles of clean code in that the function is too long, no more than 3-4 lines
    def search(self, nums: List[int], target: int) -> int:
        #no more than 1 argument passed in violated
        left = 0
        right = len(nums)-1
        
        while left <= right:
            n = (right + left)//2
            if target == nums[n]:
                return n
            elif target < nums[n]:
                right = n - 1
            elif target > nums[n]:
                left = n + 1 
        return -1
        #however, no side missions, only does one thing!
#O(log n) time && O(1) space 
