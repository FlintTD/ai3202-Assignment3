import sys
import random


class Horse(object):                                    # horse class, sort of superfluous
    x = 0
    y = 0

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def move(self, node):
        self.y = node.y
        self.x = node.x

    def location(self):
        return [self.y, self.x]

    def node(self, ymod, xmod):
        return Node(self.y + ymod, self.x + xmod)


class Node(object):
    x = 0
    y = 0

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def tweak(self, ymod, xmod):
        return Node(self.y + ymod, self.x + xmod)

    def print_node(self):
        print "[%s,%s]" % (self.y, self.x)

    def is_same(self, othernode):
        if (self.y == othernode.y) and (self.x == othernode.x):
            return True
        else:
            return False


def g_score(map, origin, destination):                  # calculates G score
    score = 0
    if map[destination.y][destination.x] is "1":
        score += 10
    if abs(origin.y - destination.y) + abs(origin.x - destination.x) == 2:
        score += 14
    else:
        score += 10
    return score


def manhattan(origin, goal):
    score = 10 * (abs(origin.y - goal.y) + abs(origin.x - goal.x))
    return score


def diagonal(origin, goal):                             # Diagonal Shortcut heuristic
    ydist = abs(origin.y - goal.y)
    xdist = abs(origin.x - goal.x)
    if ydist > xdist:
        score = (14 * xdist) + (10 * (ydist - xdist))
    else:
        score = (14 * ydist) + (10 * (xdist - ydist))
    return score


def wild_ride():                                        # THE RIDE NEVER ENDS
    score = random.randint(1, 50)
    return score


def a_star_search(map, center, goal, algcode, searched, trail, score, checks, iterkill):
    tosearch = []
    currentf = 0
    pointer = None

    pointer = center.tweak(-1, 0)                      # add all valid nodes around the center
    if (0 <= pointer.y < 8) and (0 <= pointer.x < 10):
        tosearch.append(pointer)
    pointer = center.tweak(-1, 1)
    if (0 <= pointer.y < 8) and (0 <= pointer.x < 10):
        tosearch.append(pointer)
    pointer = center.tweak(0, 1)
    if (0 <= pointer.y < 8) and (0 <= pointer.x < 10):
        tosearch.append(pointer)
    pointer = center.tweak(1, 1)
    if (0 <= pointer.y < 8) and (0 <= pointer.x < 10):
        tosearch.append(pointer)
    pointer = center.tweak(1, 0)
    if (0 <= pointer.y < 8) and (0 <= pointer.x < 10):
        tosearch.append(pointer)
    pointer = center.tweak(1, -1)
    if (0 <= pointer.y < 8) and (0 <= pointer.x < 10):
        tosearch.append(pointer)
    pointer = center.tweak(0, -1)
    if (0 <= pointer.y < 8) and (0 <= pointer.x < 10):
        tosearch.append(pointer)
    pointer = center.tweak(-1, -1)
    if (0 <= pointer.y < 8) and (0 <= pointer.x < 10):
        tosearch.append(pointer)

    scrutiny = None

    while len(tosearch) > 0:                           # evaluate all the tosearch nodes
        pointer = tosearch.pop()
        if map[pointer.y][pointer.x] is not "2":
            if trail.count(pointer) == 0:
                if algcode is "1":
                    tempscore = g_score(map, center, pointer) + manhattan(pointer, goal)
                elif algcode is "2":
                    tempscore = g_score(map, center, pointer) + diagonal(pointer, goal)
                elif algcode is "3":
                    tempscore = g_score(map, center, pointer) + wild_ride()
                if currentf == 0 or tempscore < currentf:
                    currentf = tempscore
                    scrutiny = pointer
        searched.append(pointer)
        checks += 1

    if scrutiny is None:                                # advanced pathfinding if stuck
        trail.pop()
        score.pop()
        location = trail[-1]
    else:
        location = scrutiny
        trail.append(scrutiny)                          # move best option into solution
        score.append(currentf)

    '''
    for y in trail:
        y.print_node()
    print score
    print checks
    '''
    iterkill += 1
    if location.is_same(goal):                          # if goal is reached, return
        return trail, score, checks
    elif scrutiny is None:
        return trail, score, checks
    elif iterkill > 40:                                 # emergency overflow shutdown
        return trail, score, checks
    else:                                               # if goal is not reached, iterate
        results = a_star_search(map, location, goal, algcode, searched, trail, score, checks, iterkill)
        return results[0], results[1], results[2]


def main(argv):                                         # -------MAIN----------------------------
    w = sys.argv[1]
    s = sys.argv[2]
    world = []
    with open(w) as f:                                  # read in and clean up world data
        for line in f:
            world_in_list = line.strip("\n")
            world_in_list = world_in_list.strip("\r")
            world_in_list = world_in_list.strip("")
            world_in_list = world_in_list.split(" ")
            world.append(world_in_list)
    world.pop()

    hol = Horse(7, 0)                                   # worldbuilding and execution
    origin = hol.node(0, 0)
    goal = Node(0, 9)
    path = [origin]
    searched_nodes = [origin]
    totalscore = []
    totalchecks = 0
    leash = 0

    result = a_star_search(world, origin, goal, s, searched_nodes, path, totalscore, totalchecks, leash)

    sum = 0
    for r in range(0, len(result[1])-1):
        sum += result[1][r]
    print "Path followed:"
    for yy in result[0]:
        yy.print_node()
    print "Total F-Score is: %s" % sum
    print "Total number of unique node checks: %s" % result[2]


if __name__ == "__main__":
    main(sys.argv)


# Cited Code
# http://stackoverflow.com/questions/10393176/is-there-a-way-to-read-a-txt-file-and-store-each-line-to-memory
# May 1, 2012
#
# Cited Heuristic
# http://www.policyalmanac.org/games/heuristics.htm
# By Patrick Lester - April 21, 2004