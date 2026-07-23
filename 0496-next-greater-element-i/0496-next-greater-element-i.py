class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        stack = []
        mpp = {}

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if not stack:
                mpp[nums2[i]] = -1
            else:
                mpp[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        ans = []
        for num in nums1:
            ans.append(mpp[num])

        return ans