import pandas as pd
def Hash(Current,ascValue):
    Current+=ascValue
    Current*=17
    Current%=256
    return Current
def Part1():
    inputs=pd.read_csv("input.txt",header=None).values[0].tolist()
    RunningTotal=0
    for input in inputs:
        Current=0
        for character in input:
            Current=Hash(Current,ord(character))
        RunningTotal+=Current
    print(RunningTotal)

Part1()


def LensingPower(Box):
    LP=0
    for n,nBox in enumerate(Box):
        for s,sBox in enumerate(nBox):
            LP+=int(sBox[-1])*(s+1)*(n+1)
    print(LP)
def Part2():
    inputs=pd.read_csv("input.txt",header=None).values[0].tolist()
    RunningTotal=0
    Box=[ [] for i in range(256)]

    for input in inputs:
        Current=0
        RunningTotal=0
        for j,character in enumerate(input):
            if character in "=-":
                break
            else:
                Current=Hash(Current,ord(character))
         
        RunningTotal+=Current
        if character == "-":

            
            for k,elements in enumerate(Box[RunningTotal][:]):
                # print(RunningTotal,k)
                if Box[RunningTotal][k][:Box[RunningTotal][k].find("=")]==input[:j]:
                    # print(Box[RunningTotal][k],input)
                    Box[RunningTotal][k]=None

            Box[RunningTotal]=[x for x in Box[RunningTotal] if x is not None]

        else:

            if input[:j] not in [x[:x.find("=")] for x in Box[RunningTotal][:]]:
                Box[RunningTotal]+=[input]
            else :
                for k,elements in enumerate(Box[RunningTotal][:]):
                    if Box[RunningTotal][k][:Box[RunningTotal][k].find("=")]==input[:j]:
                        Box[RunningTotal][k] = input  


    LensingPower(Box)
    
Part2()

    
