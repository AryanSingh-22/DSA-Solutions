class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle the one special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            
            # Double the divisor as long as it still fits
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the biggest chunk that fit
            dividend -= temp_divisor
            quotient += multiple
        
        result = -quotient if negative else quotient
        
        # Clamp to 32-bit range
        return max(INT_MIN, min(INT_MAX, result))