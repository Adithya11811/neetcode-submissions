class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,h = 0, len(nums)-1

        while l <= h:
            
            m = (l+h)//2
            print("l,h,m=",l,h,m)
            if target == nums[m]:
                return m

            if target < nums[m]:
                h = m -1

            else:
                l = m+1

        
        return -1