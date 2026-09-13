class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #brute force -> 


        cars=sorted(zip(position,speed),reverse=True)
        maxT,fleet=0,0

        for pos, spd in cars:
            time=(target-pos)/spd

            if time>maxT:
                maxT=time
                fleet+=1
        return fleet