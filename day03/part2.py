import re

answer = 0
re_dont = "don\'t()"

with open('day03/input.txt', 'r') as file:
    do = True
    for memory in file:
        all_matches = re.findall('mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)|do\(\)|don\'t\(\)', memory) 
        
        for match in all_matches:
            z = re.findall('[1-9][0-9]{0,2},[1-9][0-9]{0,2}', match)
            if z:
                if do:
                    x, y = z[0].split(',')
                    answer += int(x) * int(y)
            elif match == re_dont:
                do = False
            else:
                do = True 
        
    print(answer)
        