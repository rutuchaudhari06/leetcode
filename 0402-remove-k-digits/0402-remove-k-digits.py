class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for x in num:
            while st and k > 0 and st[-1] > x:
                st.pop()
                k -= 1

            st.append(x)

        while k > 0:
            st.pop()
            k -= 1
        ans=''.join(st).lstrip('0')
        return ans or "0"