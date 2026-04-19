class Solution:
    def reverseBits(self, n: int) -> int:
        
        ans = 0
        i = 32
        while i!=0:
            t=0
            t = n&1
            n >>=1
            ans<<=1
            ans = ans | t
            i-=1

        return ans