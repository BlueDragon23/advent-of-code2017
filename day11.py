def get_coord(seq):
    coord = (0, 0) # x, y
    for direction in seq:
        x = coord[0]
        y = coord[1]
        if direction == 'N':
            y += 2
        elif direction == 'S':
            y -= 2
        elif direction == 'NE':
            x += 1
            y += 1
        elif direction == 'SE':
            x += 1
            y -= 1
        elif direction == 'NW':
            x -= 1
            y += 1
        elif direction == 'SW':
            x -= 1
            y -= 1
        coord = (x, y)
    return coord

if __name__=="__main__":
    f = open("input11.txt")
    seq = []
    for line in f:
        seq.extend([s.upper() for s in line.strip().split(',')])
    max_steps = 0
    for i in range(len(seq)):
        final_coord = get_coord(seq[:i+1])
        smaller = min(abs(final_coord[0]), abs(final_coord[1]))
        final_coord = (abs(abs(final_coord[0]) - smaller), abs(abs(final_coord[1]) - smaller))
        rest = final_coord[0] if final_coord[0] != 0 else final_coord[1]
        total = smaller + abs(rest/2)
        print(total)
        if total > max_steps:
            max_steps = total
    print(max_steps)
        
        
