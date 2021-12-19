 
import sys

def calc(argv):
    with open(argv,'r') as f:
        measurements = f.readlines()
        measurements = [measure.rstrip() for measure in measurements] #data file seemed to have \n at the end of each line
    counter = 0
    for count, measure in enumerate(measurements[1:]):
        if int(measure) > int(measurements[count-1]):
            counter += 1
    return counter

if __name__ == '__main__':
    print(calc(sys.argv[1]))