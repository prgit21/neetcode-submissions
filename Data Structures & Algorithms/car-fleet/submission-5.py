class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car forms fleet only when the time for the car ahead of it is more
        #time=d/sp
        #zip and reverse it, so u can iterate in a single array 

        fleet,maxt=0,0

        cars=sorted(zip(position,speed),reverse=True)

        for pos,spd in cars:
            # calc dist and time

            time=(target-pos)/spd

            if time>maxt:
                fleet+=1
                maxt=time
        return fleet
