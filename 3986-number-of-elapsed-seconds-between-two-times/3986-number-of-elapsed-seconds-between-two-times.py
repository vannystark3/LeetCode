class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        hrs = int(endTime[0:2])-int(startTime[0:2])
        mins = int(endTime[3:5])-int(startTime[3:5])
        secs = int(endTime[6:])-int(startTime[6:])
        total = secs + mins*60 + hrs*60*60
        return total