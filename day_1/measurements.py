 
import sys

def calc(argv):
    with open(argv,'r') as f:
        measurements = f.readlines()
        measurements = [measure.rstrip() for measure in measurements] #data file seemed to have \n at the end of each line
    counter = 0
    sum_counter = 0
    previous_sum = 0
    for index in range(len(measurements) - 1):
        if int(measurements[index + 1]) > int(measurements[index]):
            counter += 1
        previous_sum = int(measurements[index - 1]) + int(measurements[index]) + int(measurements[index + 1])
        try:
            current_sum = int(measurements[index]) + int(measurements[index + 1]) + int(measurements[index + 2])
        except:
            continue
        if current_sum > previous_sum:
            sum_counter += 1
    return counter, sum_counter

if __name__ == '__main__':
    print(calc(sys.argv[1]))