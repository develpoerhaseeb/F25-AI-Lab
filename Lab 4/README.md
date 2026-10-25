
## Files

- `lab4_astar_audit.py` – contains all the code in one file: A* and UCS search, Task 1 check, audit Task 2 (A* versus UCS) and Task 3 (overestimate experiment).

- `Lab4_output.txt` – holds the captured output of the complete run.

- `Lab4_Report.docx` – the full lab report.

## Setup and run

Requires Python 3.8 or newer. No external packages are needed; the code imports the standard library module `math`.

```

python lab4_astar_audit.py

```

To run a single part modify the variable `RUN` near the bottom of the file to `"task1"` `"task2"` or `"task3"`.

To save the output in a file:

```

python lab4_astar_audit.py > lab4_output.txt

```

## What it does

1. Task 1 check – prints the frontier table for the three expansions so that it can be compared with the hand calculation.

2. Audit – verifies that the heuristic is admissible and consistent.

3. Task 2 – runs A* using the supplied heuristic and runs UCS (with all h values set to zero) on the same graph.

4. Task 3 – modifies h(C) from 2 to 10 reruns A*. Then compares the outcome with the original run. It also tests the case where h(C) equals 4.

## Input

Graph and heuristic definitions appear at the top of the code taken from the lab manual, for Lab 4 pages 16 to 17.

## Notes

- No passwords, private data or virtual environment files are included.