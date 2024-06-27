import typing
class Solution:
    def longestConsecutive(self, nums: typing.List[int]) -> int:
        nums1 = list(set(nums))
        nums1.sort()
        largestCount = 0
        for i in range(len(nums1)):
            temp = 1
            for j in range(i + 1,len(nums1)):
                if(nums1[i]  + temp == nums1[j] ):
                    temp +=1 
                else:
                    break
            largestCount = max(largestCount,temp)
        return largestCount
        


        # for i in range(5):
        #     for number in range(10):
        #         if number == 5:
        #             break    # break here

        #         print('Number is ' + str(number))

        #     print('Out of loop')