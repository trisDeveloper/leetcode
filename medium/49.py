# 49. Group Anagrams solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            if ''.join(sorted(i)) in dic:
                dic[''.join(sorted(i))] += [i]
                
            else:
                dic[''.join(sorted(i))] = [i]
                    
        return list(dic.values())
