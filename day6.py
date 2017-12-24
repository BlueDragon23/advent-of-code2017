primes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

def hash(mem):
    total = 0
    for i in range(len(mem)):
        total = 17 * total + mem[i] 
    return total

def redistribute(mem):
    maximum = max(mem)
    i = mem.index(maximum)
    mem[i] = 0
    while maximum > 0:
        i = (i + 1) % len(mem)
        mem[i] += 1
        maximum -= 1
    return mem

if __name__=="__main__":
    f = open("input6.txt")
    mem = [int(x) for x in f.readline().strip().split()]
    unique = {}
    count = 0
    while True:
        mem = redistribute(mem)
        print(mem)
        h = hash(mem)
        count += 1
        if h in unique:
            print(count)
            print(count - unique[h])
            exit(0)
        unique[h] = count
        if len(unique) % 10000 == 0:
            print(len(unique))
