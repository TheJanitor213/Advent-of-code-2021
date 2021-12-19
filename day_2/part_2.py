import sys

def coordinates(argv):
    depth, horizontal, aim = 0, 0, 0
    with open(argv,'r') as f:
        movements = f.readlines()
        movements = [movement.rstrip() for movement in movements] #data file seemed to have \n at the end of each line

    for movement in movements:
        direction, distance = movement.split((' '))
        if direction == 'forward':
            horizontal += int(distance)
            depth += (aim * int(distance)) 
        elif direction == 'up':
            aim -= int(distance)
        else:
            aim += int(distance)
    return depth * horizontal

if __name__ == '__main__':
    print(coordinates(sys.argv[1]))
