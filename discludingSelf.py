from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))
#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             print(str(i) + " prefix " + str(res) + "\n")
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             print()
#             res[i] *= postfix
#             print(str(i) + " post " + str(res) + "\n")
#             postfix *= nums[i]
#         return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums))
        sum,zerCount = 1, 0
        for num in nums:
            if num != 0:
                sum *= num
            else:
                zerCount += 1
        
        if zerCount > 1:
            return res
        
        if zerCount == 1:
            for i in range(len(nums)):
                if(nums[i]) == 0:
                    res[i] = sum
                else: 
                    res[i] = 0
        else:
            for i in range(len(nums)):
                res[i] = sum // nums[i]
        # understand thought process of how solution works instead of just the code. 
        return res


            

        
        for i in range(len(nums)):
            sum *= nums[i]
        for i in range(len(nums)):
            nums[i] = sum / nums[i]
        return nums        



        # res  = []
        # for i in range( len(nums)):
        #     temp = 1          
        #     for j in range(len(nums)):
        #         if(i != j):temp *= nums[j]
        #     res.append(temp)
        # return res

postfix = 8 * 7 

o = Solution()
print(o.productExceptSelf([5,6,7,8]))
# 1111 5678  1 5 30 210 
# 1 5 30 210 
# 336 280 240 210 
 # 1 5*30*  210 
 

# obj = set()
