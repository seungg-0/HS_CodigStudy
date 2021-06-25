from typing import List
# s = ["flower","flow","flight"]
# s = zip(*s)
# s = set(s)
# print(len(s))
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        for i in zip(*strs):
            if len(set(i)) !=1:
                return s
            else:
                s += i[0]
        return s