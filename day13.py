import datetime
def get_severity(depth, r, offset):
    # print((offset + depth) % ((r - 1) * 2))
    if (offset + depth) % ((r - 1) * 2) == 0:
        return True
    else:
        return False

def get_total_severity(d, i):
    caught = False
    for key, val in d.items():
        caught |= get_severity(key, val, i)
        if caught:
            return caught
    return caught

if __name__=="__main__":
    f = open("input13.txt")
    d = {}
    for line in f:
        s = line.strip().split(": ")
        d[int(s[0])] = int(s[1])
    i = 0
    hits = []
    print(datetime.datetime.now())
    while len(hits) < 1:
        caught = get_total_severity(d, i)
        if not caught:
            print(i)
            hits.append(i)
        i += 1
    print(hits)
    print(datetime.datetime.now())
