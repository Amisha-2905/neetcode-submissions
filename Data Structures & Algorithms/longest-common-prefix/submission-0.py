class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort(key=len)
        ok = 0
        for i in range(len(strs[0])):
            a = strs[0][i]
            for string in strs:
                if string[i] != a:
                    ok = 1
                    break
            if ok == 1:
                break
            ans += a
        return ans