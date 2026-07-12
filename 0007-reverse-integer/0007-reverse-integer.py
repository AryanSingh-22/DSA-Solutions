class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        while x != 0:
            digit = x % 10       # grab last digit
            x = x // 10          # remove last digit
            reversed_num = reversed_num * 10 + digit  # build new number
        reversed_num *= sign
        # Check the "too big" rule (32-bit limit)
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num