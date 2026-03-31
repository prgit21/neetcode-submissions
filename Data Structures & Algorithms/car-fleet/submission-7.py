class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #invariant -> if car ahead takes more time to reach then it forms a fleet woth the car ahead

        cars=sorted(zip(position,speed),reverse=True)
        maxt=0
        fleet=0

        for pos, spd in cars:
            time= (target-pos)/spd
            
            if time>maxt:
                maxt=time
                fleet+=1
        return fleet


            
        