class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0
        limit = 2147483647 if sign == 1 else 2147483648

        while x:
            digit = x % 10
            x //= 10

            if rev > (limit - digit) // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev