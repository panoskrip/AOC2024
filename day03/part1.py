import re

answer = 0

with open('day03/input.txt', 'r') as file:
    
    for memory in file:
        all_matches = re.findall('mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)', memory)    
        
        for mul in all_matches:
            z = re.findall('[1-9][0-9]{0,2},[1-9][0-9]{0,2}', mul)
            x, y = z[0].split(',')
            answer += int(x) * int(y)
        
    print(answer)