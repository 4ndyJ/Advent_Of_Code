'''
The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
'''

import pandas as pd
def D1Solution_part1(file,total=0):
    Data=pd.read_csv(file,header=None).values
    for data in Data:
        nums=numbers(data[0],[])
        if len(nums)==1:
            nums+=[nums[-1]]
        first, *_, last= nums
        concat=int(str(first)+str(last))
        total+=concat
    return(total)
    
    def D1Solution_part2(file,total=0):
    Data=pd.read_csv(file,header=None).values
    
    for data in Data:
        nums,numsindex=numberspart2(data[0],[],[])
        wordsnums,wordsindex=WordsToNumbers(data[0],[],[])
        
        FullList=list(zip(numsindex,nums))+list(zip(wordsindex,wordsnums))
        
        nums=list(list(zip(*sorted(FullList)))[1])
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

def numberspart2(string,numbers=[],index=[]):
    for i,s in enumerate(string):
        try:
            number=int(s)
        except:
            continue
    
        numbers+=[number]
        index+=[i]
    return(numbers,index)
    
def WordsToNumbers(String,wordsnums=[],wordsindex=[]):
    
    spelt_numbers={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    kernel=5
    for spelt in spelt_numbers.keys():
        for j in range(len(String)):
            if spelt in String[j:j+kernel]:
                i=String[j:j+kernel].find(spelt)
                wordsindex+=[i+j]
                wordsnums+=[spelt_numbers[spelt]]
    return(wordsnums,wordsindex)
    
D1Solution_part1("input.txt")
D1Solution_part2("inpit.txt",0)
