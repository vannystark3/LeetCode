class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        ind = -1
        l = len(drones)
        tx,ty = target
        mini = float('inf')
        for i in range(l):
            x,y,tr = drones[i]
            manhdis = abs(x-tx)+abs(y-ty)
            if manhdis<=tr and manhdis<mini:
                mini = manhdis
                ind = i
        return ind