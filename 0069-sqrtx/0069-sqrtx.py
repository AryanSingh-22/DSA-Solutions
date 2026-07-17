class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x
        ans = 0

        while start <= end:
            mid = start + (end - start) // 2

            if mid * mid == x:
                ans = mid
                break
            elif mid * mid < x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1

        return ans