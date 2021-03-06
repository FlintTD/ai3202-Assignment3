# ai3202-Assignment3
A* Search implementation.  I had no clue how to make directories in Git, so I did this filename instead.


The command line inputs are simple: worldName.txt followed by heuristicNumber
The two given worlds are in this repository.  Heuristic 1 (just type in 1) is Manhattan distance. Heuristic 2 is Diagonal Shortcut, which encourages diagonal moves toward the goal.  Heuristic 3 is Mister Bones' Wild Ride, which puts a randomizer from 1 to 50 instead of a heuristic.


Heuristic 2:

The world maps that were given to us often looked complicated near the edges, but more forgiving near the middle.  I wanted to see if a heuristic that encouraged staying to the middle of the map would improve my score at all.


H2(n) =
  if |y distance between goal and n| > |x distance between goal and n| :
    (14 * |distance x|) + (10 * |distance y| - |distance x|)
  OR
  if |y distance between goal and n| < |x distance between goal and n| :
    (14 * |distance y|) + (10 * |distance x| - |distance y|)


Somehow, Heuristic 2 managed to find two very similar paths between the two worlds, which both equated to 702 points.  Either way, Heuristic 2 recieved better scores from both worlds.

SCORES:
H1 W1:[7,0] [6,1] [5,1] [4,1] [3,1] [2,2] [2,3] [1,4] [0,5] [0,6] [0,7] [0,8] [0,9]
  Total: 976 points, 79 squares explored
H2 W1:[7,0] [7,1] [7,2] [6,3] [5,4] [4,4] [3,5] [3,6] [2,7] [2,8] [1,9] [0,9]
  Total: 702 points, 74 squares explored
H1 W2:[7,0] [6,1] [5,0] [4,1] [4,2] [4,3] [3,4] [3,5] [3,6] [2,7] [1,8] [0,9]
  Total: 1024 points, 80 squares explored
H2 W2:[7,0] [7,1] [7,2] [6,3] [5,3] [4,4] [3,5] [3,6] [2,7] [1,8] [0,9]
  Total: 702 points, 69 squares explored


Heuristic 3:

The Wild Ride did manage to end up at the goal, seemingly without direction.

H3 W2:[7,0] [7,1] [6,0] [6,1] [6,0] [7,1] [7,2] [7,1] [6,0] [7,0] [7,1] [6,1] [7,0] [6,1] [7,1] [7,0] [6,0] [7,0] [6,0] [6,1] [7,1] [7,0] [6,1] [5,0] [4,0] [5,0] [6,0] [5,0] [6,1] [5,0] [4,1] [4,0] [5,0] [6,0] [5,0] [6,0] [6,1] [5,0] [4,0] [4,1] [4,2] [4,1]
  Total: 954 points, 223 squares explored
