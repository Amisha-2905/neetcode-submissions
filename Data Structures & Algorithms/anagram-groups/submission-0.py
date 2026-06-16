class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for strings in strs:
            key = ''.join(sorted(strings))
            anagram_dict[key].append(strings)

        return list(anagram_dict.values())