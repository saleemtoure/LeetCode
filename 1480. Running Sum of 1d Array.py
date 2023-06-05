nums=[1,2,3,4]
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = 0
        rSum = []
        for num in nums:
            sums += num
            rSum.append(sums)
        return rSum


print(Solution().runningSum(nums))