class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        lmax,rmax=0,0

        ans=0
        while l<r:
            if nums[l]<=nums[r]:
                if lmax>nums[l]:
                    ans+= lmax-nums[l]
                else:
                    lmax=nums[l]
                l+=1
            else:
                if rmax>nums[r]:
                    ans+=rmax-nums[r]
                else:
                    rmax=nums[r]
                r-=1
        return ans

