class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [] # creating an empty list
        self.hashmap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        ans = ""
        values  = self.hashmap.get(key,[])
        l = 0
        r = len(values)-1 # binary search on values; finding the rightmost timestamp
        while l<=r:
            m = l+(r-l)//2 
            if values[m][1] <= timestamp:  # key : list of [val,timestamp]
                ans = values[m][0]
                l = m+1
            else:
                r = m-1
        return ans


        
