class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #car fleet forms only when the car ahad has a time longer than the car behind it
        
        cars=sorted(zip(position,speed),reverse=True)
        maxt,fleet=0,0

        for pos,spd in cars:
            # time d/s
            time=(target-pos)/spd
            if maxt<time:
                maxt=time
                fleet+=1
        return fleet