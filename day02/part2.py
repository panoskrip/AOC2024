def is_safe(level):
    diffs = [x-y for x, y in zip(level, level[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)


with open('day02/input.txt', 'r') as data:
    safeCount = 0
    for line in data:
        level = list(map(int, line.strip().split(" ") ))
        if any(is_safe(level[:i]+level[i+1:]) for i in range(len(level))):
            safeCount += 1
            
    print(safeCount)
            