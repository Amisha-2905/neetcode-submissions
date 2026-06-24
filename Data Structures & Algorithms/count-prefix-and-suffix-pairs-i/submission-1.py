class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        len_1 = len(str1)
        if len(str2) < len_1:
            return False
        pref = True
        for i in range(len_1):
            if str1[i] != str2 [i]:
                pref = False
                break
        suf = True
        len_2 = len(str2)
        diff = len_2 - len_1
        for i in range(len_1 - 1, -1, -1):
            if str1[i] != str2 [diff + i]:
                suf = False
                break
        return pref and suf
            
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        output = 0
        for i, word in enumerate(words):
            j = i + 1
            while (j < len(words)):
                # if_pref_suf = self.isPrefixAndSuffix(word, words[j])
                if self.isPrefixAndSuffix(word, words[j]):
                    output += 1
                j += 1
        return output