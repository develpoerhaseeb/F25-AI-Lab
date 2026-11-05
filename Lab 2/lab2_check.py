#lab 2 -- Feflex Agent --
class classroomagent:
    def act(self,temp,occupied):
        if not occupied:
            return"ECO"
        if temp>26:
            return "COOL"
        if temp<20:
            return "WARM"
        return "IDLE"

if __name__ == "__ main __":
    agent=classroomagent()
    percepts=[(29, True),(29, True),(20, True),(26, True),(19, True),(29, True)]
    for step, percept in enumerate(percepts,1):
        print(step,"target mode", agent.act(*percept))