class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = len(nums) * [1]
        suffix = len(nums)* [1]
        products = {}
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(suffix)-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        answers = [prefix[x] * suffix [x] for x in range(len(nums))]
        return answers

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))