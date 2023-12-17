from sortedcontainers import SortedList
from collections import deque

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.sorted_list = SortedList()
        self.deque = deque()

    def addElement(self, num: int) -> None:
        if len(self.sorted_list) >= self.m:
            oldest_val = self.deque.popleft()
            self.sorted_list.discard(oldest_val)
        
        self.sorted_list.add(num)
        self.deque.append(num)
        

    def calculateMKAverage(self) -> int:
        if (len(self.sorted_list) < self.m):
            return -1
        
        middle_elements = self.sorted_list[self.k:-self.k]
        return int(sum(middle_elements)/len(middle_elements))
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()