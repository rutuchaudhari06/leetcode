class StockSpanner:

    def __init__(self):
        self.st=[]
        self.idx=-1

        

    def next(self, price: int) -> int:
        self.idx+=1
        while self.st and self.st[-1][1]<=price:
            self.st.pop()
        ans=self.idx-(-1 if not self.st else self.st[-1][0])
        self.st.append((self.idx,price))
        return ans
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)