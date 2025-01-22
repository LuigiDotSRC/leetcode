from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# class TimeMap:

#     def __init__(self):
#         self.kvs = defaultdict(list)

#     # O(1) all calls to set are in increasing order therefore order is maintained 
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         self.kvs[key].append((value, timestamp)) 

#     # O(logn) O(m*n) space
#     def get(self, key: str, timestamp: int) -> str:
#         values = self.kvs[key]

#         if values[0][1] > timestamp:
#             return ""
        
#         # binary search the values
#         l, r = 0, len(values)
#         mid, prev = l, l
#         while l <= r:
#             mid = l + (r - l) // 2
            
#             if l == r:
#                 if values[l][1] == timestamp:
#                     return values[l][0]
#                 else:
#                     return values[prev][0]

#             prev = mid

#             # search bottom half
#             if values[mid][1] > timestamp:
#                 r = mid - 1

#             # search top half
#             else:
#                 l = mid + 1

#         return values[mid][0]
