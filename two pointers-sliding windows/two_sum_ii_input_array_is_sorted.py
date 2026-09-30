class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []  # Return an empty list if no solution is found
    
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))