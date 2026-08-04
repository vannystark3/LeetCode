class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxi = ""
        first = strs[0]
        mini = float('inf')
        for word in strs:
            mini = min(mini,len(word))
        if mini==0:
            return ""
        l = len(strs)
        i=0
        while i<mini:
            for word in strs:
                if word[i]!=first[i]:
                    return maxi
            maxi += first[i]
            i += 1
        return maxi