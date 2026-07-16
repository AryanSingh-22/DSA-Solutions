class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        # Step 2: check for sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        # Step 3: read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1
        # Step 4: apply sign
        num *= sign
        # Step 5: clamp to 32-bit range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        return num