class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        maxarea=0
        n=len(nums)

        st=[]

        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                el=st.pop()
                nse=i 
                pse= -1 if not st else st[-1]
                maxarea=max(maxarea,nums[el] * (nse-pse-1))
            st.append(i)    
        while st:
            el = st.pop()
            nse = n
            pse = -1 if not st else st[-1]
            maxarea = max(maxarea, nums[el] * (nse - pse - 1))      
        return maxarea


        