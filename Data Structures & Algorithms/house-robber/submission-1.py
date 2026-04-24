from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def kp(i):
            if i >= n:
                return 0

            pick = nums[i] + kp(i+2)
            nopick = kp(i+1)

            return max(pick, nopick)

        return kp(0)