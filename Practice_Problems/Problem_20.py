import os


class Solution(object):
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
