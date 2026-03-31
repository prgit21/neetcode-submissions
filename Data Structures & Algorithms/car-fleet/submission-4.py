class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car forms fleet only when the time for the car ahead of it is more
        #time=d/sp
        #zip and reverse it, so u can iterate in a single array 

        fleet,maxt=0,0
        cars=sorted(zip(position,speed),reverse=True)  #sort cars by positin ,speed and then ensure in closest from tatget 

        for pos,spd in cars:
            # calculate time left for each car
            time=(target-pos)/spd
            # if time is more than the car behind then fleet
            if time>maxt:
                fleet+=1
                maxt=time
        return fleet
