class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mpp={}
        for ch in tasks:
            mpp[ch]=mpp.get(ch,0)+1
        
        pq=[(-freq,key) for key,freq in mpp.items()]
        heapq.heapify(pq)
        cooldown=deque()

        time=0

        while pq or cooldown:
            time+=1
            if pq:
                freq,task=heapq.heappop(pq)
                freq+=1

                if freq!=0:
                    cooldown.append((time+n,freq,task))
            
            if cooldown and cooldown[0][0]==time:
                avail,count,task=cooldown.popleft()
                heapq.heappush(pq,(count,task))
        return time


        