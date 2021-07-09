# Kitchen-Task

You are given a building floor map like so:

WWWWWWWWWWWWW
W E   W E   W
W	W	W
W           W
W	W     W
W E	W E   W
WWWWWWWWWWWWW

W - wall
E - employee
[SPACE] - empty space

The goal is to find the best empty space to put a kitchen in.
The kitchen needs to be located in the empty space for which the sum of distances to all employees is minimal.
The distance from an empty space to an employee is the shortest path from the employee to the empty space.
Employees can only walk in north, south, east or west directions (no diagonals).
Employees cannot walk through walls (of course).

The Solution was implemented by BFS Algorithm in Python Language.  
