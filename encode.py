from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        stringOutput = ""
        for i in strs:
            stringOutput += i + "†"
        print(stringOutput)
        return stringOutput

    def decode(self, s: str) -> List[str]:
        startValue = 0
        endValue = 0
        newList = []
        for i in range(len(s)):
            if (s[i] == "†"):
                endValue = i
                storedValue = ""
                incrementer = 0
                for j in range(startValue, endValue):
                    storedValue += s[j]
                newList += [storedValue]
                if (i != len(s)):
                    startValue = i + 1

        return newList

    def twoSum(self, s: List[int], k: int) -> List[int]:
        # obj = {}
        # for i, n in enumerate(s):
        #     diff = k - n
        #     if (diff in obj):
        #         return [obj[diff], i]
        #     obj[n] = i
        # return []
        for i in range(len(s)):
          for j in range(i+1, len(s)):
            if(s[i] + s[j] == k): return [i,j]


s = "asa"
print(s[1])
obj = Solution()
# lis = ["asdfas", "asdfa", "asas"]

# print(obj.decode(obj.encode(lis)))
print(obj.twoSum([1, 2, 3, 4], 5))
