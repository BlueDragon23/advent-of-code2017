def redistribute(mem):
    maximum = max(mem)
    i = mem.index(maximum)
    mem[i] = 0
    while maximum >= 0:
        i = (i + 1) % len(mem)
        mem[i] += 1
        maximum -= 1
    return mem

if __name__=="__main__":
    f = open("input6.txt")
    mem = tuple([int(x) for x in f.readline().strip().split()])
    mem_list = list(mem)
    unique = set()
    unique.add(mem)
    count = 0
    while True:
        mem_list = redistribute(mem_list)
        mem = tuple(mem_list)
        count += 1
        if mem in unique:
            print(count)
            exit(0)
        unique.add(mem)
        if len(unique) % 10000 == 0:
            print(len(unique))
