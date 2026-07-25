class Solution:
    def findnse(self,nums):
        n=len(nums)
        nse=[n]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            nse[i]=n if not st else st[-1]
            st.append(i)
        return nse

    def findpse(self,nums):
        n=len(nums)
        pse=[-1]*n
        st=[]
        for i in range(n):
            while st and nums[i]<nums[st[-1]]:
                st.pop()
            pse[i]= -1 if not st else st[-1]
            st.append(i)
        return pse

    def largestRectangleArea(self, nums: List[int]) -> int:
        nse=self.findnse(nums)
        pse=self.findpse(nums)
        maxarea=0
        n=len(nums)

        for i in range(n):
            maxarea=max(maxarea,nums[i] * (nse[i]-pse[i]-1))
        return maxarea


        