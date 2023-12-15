import pandas as pd
def Hash(Current,ascValue):
    Current+=ascValue
    Current*=17
    Current%=256
    return Current
inputs=pd.read_csv("input.txt",header=None).values[0].tolist()
RunningTotal=0
for input in inputs:
    Current=0
    for character in input:
        Current=Hash(Current,ord(character))
    RunningTotal+=Current
print(RunningTotal)
