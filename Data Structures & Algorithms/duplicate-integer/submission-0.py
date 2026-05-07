class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = len(set(nums))
        
        if result < len(nums):
            return True
        
        return False