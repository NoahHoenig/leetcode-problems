class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, val in enumerate(nums):
            complement = target - val

            if complement in seen:
                return [seen[complement], i]
            else:
                seen[val] = i


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))