class Solution:
    def mySqrt(self, x: int) -> int:
        l,h = 1, x

        while l <= h:
            m = (l+h)//2

            if m == x//m:
                return m

            if m > x/m:
                h = m-1
            else:
                l = m+1

        return l-1