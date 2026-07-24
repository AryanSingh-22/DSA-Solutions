class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        
        result = [0] * len(nums)
        
        for i in range(len(positives)):
            result[2 * i] = positives[i]       # even index: 0, 2, 4...
            result[2 * i + 1] = negatives[i]   # odd index: 1, 3, 5...
        
        return result