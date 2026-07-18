class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        score = None
        count = 0

        for num in nums:
            if count == 0:
                score = num
            if num == score:
                count += 1
            else:
                count -= 1
        return score
