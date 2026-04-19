class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        i = 0
        while i <= n:
            t = i
            cnt = 0
            while t != 0:
                if t&1:
                    cnt+=1
                t >>= 1

            ans.append(cnt)
            i += 1

        return ans