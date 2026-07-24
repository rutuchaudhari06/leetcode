class Solution:
    def findnse(self,nums):
        nse=[0]*len(nums)
        st=[]
        for i in range(len(nums)-1,-1,-1):
            while st and nums[i]<=nums[st[-1]]:
                st.pop()
            nse[i]=len(nums) if not st else st[-1]
            st.append(i)

        return nse
    
    def findpsee(self,nums):
        psee=[0]*len(nums)
        st=[]
        for i in range(len(nums)):
            while st and nums[i]<nums[st[-1]]:
                st.pop()
            psee[i]= -1 if not st else st[-1]
            st.append(i)
        return psee
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        nse=self.findnse(arr)
        psee=self.findpsee(arr)
        total=0
        mod=10**9+7
        for i in range(n):
            left=i-psee[i]
            right=nse[i]-i
            total = (total + left * right * arr[i]) % mod
        return total
        
