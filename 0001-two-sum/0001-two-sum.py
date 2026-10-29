class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in seen:
                return (seen[missing], i)
            seen[nums[i]] = i