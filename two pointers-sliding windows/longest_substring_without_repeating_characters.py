class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_seen = {}
        left = 0
        for idx, ch in enumerate(s):
            while ch in char_seen: 
                
                char_seen.pop(s[left])
                left += 1
            char_seen[ch] = idx
            max_length = max(max_length, idx - left + 1)
        return max_length
