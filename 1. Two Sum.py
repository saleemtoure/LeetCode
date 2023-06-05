nums = [2,7,11,15]
target=9
class Solution(object):
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return i,j

print(Solution().twoSum(nums,target))