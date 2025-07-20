class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        memo = set()
        for num in nums:
            if num in memo:
                return True
            memo.add(num)

        return False
