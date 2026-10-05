class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subset = []
        result = []
        def backtrack(start):
            result.append(subset.copy())
            print(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()


        backtrack(0)
        return result