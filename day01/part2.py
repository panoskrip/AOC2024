input = open('day01/input.txt', 'r')

arrX = []
arrY = []
for line in input:
    x, y = line.strip().split()
    arrX.append(int(x))
    arrY.append(int(y))

score = sum(n*arrY.count(n) for n in arrX)
 
print(score)