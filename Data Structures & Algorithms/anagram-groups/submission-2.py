class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            anagram_dict[key].append(strs[i])
        return list(anagram_dict.values())
            