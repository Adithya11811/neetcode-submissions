class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkval(k):
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)  # no need for float()
            return totalTime

        lo, hi = 1, max(piles)
        res = hi

        while lo <= hi:
            mid = (lo + hi) // 2

            if checkval(mid) <= h:  # now correctly uses the input h
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return res