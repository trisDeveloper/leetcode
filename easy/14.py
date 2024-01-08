# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        p = strs[0]
        for string in strs[1:]:
            while string.find(p) != 0:
                p = p[:-1]
                if not p:
                    return ""
        return p
