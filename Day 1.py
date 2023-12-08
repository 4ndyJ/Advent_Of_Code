'''
The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
'''

import pandas as pd
def D1Soltution_part1(file,total=0):
    Data=pd.read_csv(file,header=None).values
    for data in Data:
        nums=numbers(data[0],[])
        if len(nums)==1:
            nums+=[nums[-1]]
        first, *_, last= nums
        concat=int(str(first)+str(last))
        total+=concat
    return(total)
    
def numbers(string,numbers=[]):
    for s in string:
        try:
            number=int(s)
        except:
            continue
        numbers+=[number]
    return(numbers)

D1Soltution_part1("input.txt")
