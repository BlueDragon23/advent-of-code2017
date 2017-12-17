import math
import collections

if __name__=="__main__":
    f = open("input4.txt")
    count = 0
    for line in f:
        line = line.strip().split()
        s = set(line)
        if len(s) == len(line):
            cs = [collections.Counter(x) for x in line]
            valid = True
            for i in range(len(cs)):
                if any(cs[i] == c_iter for c_iter in (cs[:i] + cs[i+1:])):
                    valid = False
            if valid:
                count += 1
    print(count)
