from typing import List
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      obj = {}
      for i,value in enu 
      merate(nums):
          diff = target - value
          if diff in obj:
              return [i, obj[diff]]
          obj[value] = (diff)
      return []

nums = [1,5,3,2]

firstSolution = Solution()

print(firstSolution.twoSum(nums,5))



  # obj = set()
  # previousMap = {}
  # for i, n in enumerate(nums):
  #     diff = target - n
  #     if(diff in previousMap):
  #         return [previousMap[diff], i]
  #     previousMap[n] = i
