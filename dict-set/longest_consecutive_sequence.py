class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        seen = set(nums)
        longest = 0

        for i in seen:
            if i - 1 not in seen:
                starting = i
                length = 1
                while starting + length in seen:
                    length += 1
                longest = max(longest, length)

        return longest 

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))