

if __name__=="__main__":
    f = open("input5.txt")
    instr = [int(line) for line in f]
    index = 0
    num_steps = 0
    while index >= 0 and index < len(instr):
        new_index = index + instr[index]
        if instr[index] < 3:
            instr[index] += 1
        else:
            instr[index] -= 1
        index = new_index
        num_steps += 1
    print(num_steps)
