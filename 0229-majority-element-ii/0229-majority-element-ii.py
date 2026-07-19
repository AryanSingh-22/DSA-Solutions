class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        # Step 1: Find up to 2 candidates
        cand1, cand2 = None, None
        count1, count2 = 0, 0 
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        # Step 2: Verify candidates
        result = []
        n = len(nums)
        for cand in [cand1, cand2]:
            if nums.count(cand) > n // 3:
                result.append(cand)
        return result