import functools
import operator

def hash(string):
    lengths = [ord(x) for x in string]
    lengths.extend([17,31,73,47,23])
    state = list(range(256))
    skip = 0
    current = 0
    for _ in range(64):
        for length in lengths:
            if length == 1:
                pass
            elif current + length > len(state):
                sub = state[current:] + state[:(current + length) % len(state)]
                sub = list(reversed(sub))
                state[current:] = sub[:len(state) - current]
                state[:(current + length) % len(state)] = sub[len(state) - current:]
            else:
                sub = state[current:current+length]
                sub = list(reversed(sub))
                state[current:current+length] = sub
            current = (current + length + skip) % len(state)
            skip += 1
    
    dense = [functools.reduce(operator.xor, state[x:x+16]) for x in range(0,256,16)]
    
    return ''.join(['{0:0>2x}'.format(x) for x in dense])

if __name__=="__main__":
    f = open("input10.txt")
    print(hash(f.readline().strip()))
