class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strdig = ''.join(map(str,digits))
        added = int(strdig)+1
        newstrlist = list(map(int,str(added)))
        return newstrlist
        