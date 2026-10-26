# Lab 2 - sir rasikh na lab 2 maa AC wala cde krwia thaa 
 
from lab2_percepts import ClassroomAgent
from lab2_model import StatefulClassroomAgent

reflex = ClassroomAgent()
tests = [((29, True), "COOL"), ((20, True), "IDLE"), ((26, True), "IDLE"),

((19, True), "WARM"), ((29, False), "ECO"), ((15, False), "ECO")]
 
for percept, expected in tests:
    assert reflex.act(*percept) == expected, percept
print("Reflex agent: all", len(tests), "checks passed")
 

s = StatefulClassroomAgent()

assert s.act(29, True) == ("COOL", True)    
assert s.act(29, True) == ("COOL", False)   
assert s.act(24, True) == ("IDLE", True)   
assert s.act(29, False) == ("ECO", True)    
assert s.act(15, False) == ("ECO", False)   
print("Stateful agent: all checks passed")
 