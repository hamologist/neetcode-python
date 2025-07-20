class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        memo = {}
        for index in range(0, len(nums)):
            if target - nums[index] in memo:
                return [memo[target - nums[index]], index]

            memo[nums[index]] = index

        return []
