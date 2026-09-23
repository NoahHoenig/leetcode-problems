class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #freq = [0] * 26
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            #freq[ord(i.lower())-ord('a')] += 1
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return(list(groups.values()))

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))