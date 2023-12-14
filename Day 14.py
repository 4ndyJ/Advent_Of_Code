import pandas as pd
import numpy as np
data=pd.read_csv("input.txt",header=None)
# data.reindex(index=data.index[::-1])
DataList=data.values.tolist()

def north2(DataList,Output):
    for i in range(1,len(DataList)):
        for j in range(len(DataList[i][0])):
            if DataList[i][0][j]=="O":
                for k in range(1,i+1):
                    if Output[i-k][0][j] in "O#":
                        break
                Output[i][0]=Output[i][0][:j]+"."+Output[i][0][j+1:]
                if Output[i-k][0][j] in "O#":
                    Output[i-(k-1)][0]=Output[i-(k-1)][0][:j]+"O"+Output[i-(k-1)][0][j+1:]
                else:
                    Output[i-k][0]=Output[i-k][0][:j]+"O"+Output[i-k][0][j+1:]
    return Output


def west2(DataList,Output):

    for i,Data in enumerate(DataList):
        for j in range(1,len(Data[0])):
            if Data[0][j]=="O":
                for k in range(1,j+1):
                    if Data[0][j-k] in "#O":

                        break
                Output[i][0]=Output[i][0][:j]+"."+Output[i][0][j+1:]

                if Output[i][0][j-k] in "O#":
                    
                    Output[i][0]=Output[i][0][:j-k+1]+"O"+Output[i][0][j-k+2:]
                else:
                    Output[i][0]=Output[i][0][:j-k]+"O"+Output[i][0][j-k+1:]


    return Output

def east2(DataList,Output):
    reversed = [[Data[0][::-1]] for Data in DataList]
    Output=west2(reversed,np.copy(reversed))
    Output=[[Data[0][::-1] ] for Data in Output]
    
    return Output

def south3(DataList,Output):
    reversed=DataList[::-1]
    Output=north2(reversed,np.copy(reversed))
    Output=Output[::-1]
    return Output

def move(DataList,Direction):

    Output=np.copy(DataList)

    if Direction%4==0:
        Output=north2(DataList,Output)
    elif Direction%4==1:
        Output=west2(DataList,Output)
    elif Direction%4==2:
        Output=south3(DataList,Output)
    else:
        Output=east2(DataList,Output)
    if np.array_equal(DataList,Output):
        Direction+=1
        if Direction%4==0:
            return Output
    
    Output= move(Output,Direction)
    return Output
  
def Counter(DataList):
    total=0
    for i,rows in enumerate(DataList[::-1]):
        total+=(i+1)*rows[0].count("O")
    print(total)
    return(total)

from tqdm import tqdm
for i in tqdm(range(1000000000)): 
    DataList=move(DataList,0)

Counter(DataList)
