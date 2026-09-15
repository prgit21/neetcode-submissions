class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars=sorted(zip(position,speed),key = lambda c:c[0], reverse=True)
        maxT,fleets=0,0

        for pos,spd in cars:
            time = (target-pos)/spd

            if time>maxT:
                fleets+=1
                maxT=time
        return fleets
