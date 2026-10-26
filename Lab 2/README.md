
# Lab 2: Intelligent Agents


## Files
- `lab2_percepts.py` - Contains the reflex agent code.
- `lab2_model.py` - Contains the stateful agent code.
- `lab2_check.py` - Checks both agents.
- `output_percepts.txt` - Shows the reflex agent output.
- `output_model.txt` - Shows the stateful agent output.
- `output_check.txt` - Shows the test results.

## Requirements
- Python 3 must be installed.
- No extra libraries are needed.

## How to Run

Open the terminal in this folder and run these commands:

```bash
python lab2_percepts.py
python lab2_model.py
python lab2_check.py
```

## Agent Rules
- If the room is empty, select ECO.
- Below 20°C, select WARM.
- Above 26°C, select COOL.
- At 20°C and 26°C, select IDLE.

The stateful agent remembers the last mode and sends a command only when the mode changes.

## Tests
The tests check repeated inputs, temperature limits, mode changes and empty-room conditions.

Run `lab2_check.py` to check both agents.

## Code Reference
The basic classroom-agent rules were taken from the Lab 2 manual. The stateful code and tests were made for this lab.
