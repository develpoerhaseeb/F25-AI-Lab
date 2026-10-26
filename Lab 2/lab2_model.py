# Lab 2 - Stateful agent 
 
class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = None   
 
    def decide(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"
 
    def act(self, temp, occupied):
        target = self.decide(temp, occupied)
        send = target != self.previous_mode
        self.previous_mode = target
        return target, send
 
 
def run_trace(title, percepts):
    agent = StatefulClassroomAgent()
    print("\n" + title)
    print(f"{'Step':<5}{'Previous':<10}{'Percept':<14}{'Target':<8}Outcome")
    for step, percept in enumerate(percepts, 1):
        prev = agent.previous_mode
        target, send = agent.act(*percept)
        outcome = "SEND COMMAND" if send else "no command"
        print(f"{step:<5}{str(prev):<10}{str(percept):<14}{target:<8}{outcome}")
 
 
if __name__ == "__main__":
    run_trace("A) Repeated percepts", [(29, True), (29, True), (29, True)])
    run_trace("B) Exact boundaries", [(20, True), (26, True)])
    run_trace("C) Mode transition", [(29, True), (24, True), (19, True), (29, True)])
    run_trace("D) Empty room", [(29, True), (29, False), (15, False), (29, True)])
    run_trace("E) Full required sequence",
              [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)])
    run_trace("F) Noisy sequence around 26 (no hysteresis)",
              [(26.2, True), (25.8, True), (26.3, True), (25.7, True)])