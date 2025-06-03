class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        issorted = True
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                issorted = False
        return issorted
        

