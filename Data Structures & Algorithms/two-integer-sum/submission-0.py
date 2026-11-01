class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,ch in enumerate(nums):
            total = target - ch 
            if total in seen:
                return [seen[total],i]
            seen[ch] = i   
        return []     