class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n ==1 :
            return nums[0]

        dp = [[-1]* 2 for _ in range(n)]
        
        def solve(i, flg):
            if i >= len(nums) or (flg and i == n-1):
                return 0

            if dp[i][flg] != -1:
                return dp[i][flg]

            pick = nums[i] + solve(i+2, flg)
            nopick = solve(i+1, flg)

            dp[i][flg] = max(pick, nopick)
            return dp[i][flg]

        return max(solve(0, True), solve(1, False))