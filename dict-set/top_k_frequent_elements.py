class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sorted_freq = sorted(freq.items(), key=lambda pair: pair[1], reverse = True)
        return [pair[0] for pair in sorted_freq[:k]]

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))