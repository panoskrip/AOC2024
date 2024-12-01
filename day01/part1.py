input = open('day01/input.txt', 'r')

arrX = []
arrY = []
for line in input:
    x, y = line.strip().split()
    arrX.append(int(x))
    arrY.append(int(y))
    
arrX.sort()
arrY.sort()

distance = sum(abs(arrX[i] - arrY[i]) for i in range(len(arrX)))

print(distance)