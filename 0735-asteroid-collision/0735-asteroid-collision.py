class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        n=len(nums)
        st=[]
        ans=[]

        for i in range(n):
            if nums[i]>0:
                st.append(nums[i])
            else:
                while st and st[-1]>0 and abs(nums[i])>abs(st[-1]):
                    st.pop()
                if st and abs(nums[i])==st[-1]:
                    st.pop()
                elif not st or st[-1]<0:
                    st.append(nums[i])
                        
        return st