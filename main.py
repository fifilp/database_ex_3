
import re
from action import ACTION
from graph import GRAPH

def getAction(actionStr):    
    actionStr = actionStr.strip() 
    obj  = re.match(r'(?P<AcType>[R|W])(?P<TrNum>\d+)\((?P<AcItem>.*)\)', actionStr)
    AcType = obj.group(1)
    TrNum = int(obj.group(2))
    AcItem = obj.group(3)

    return ACTION(AcType,TrNum,AcItem)


def parseSchedule(schedStr):
    actionList=[]

    schedStr = schedStr.strip()
    scheduleList = schedStr.split(';')
    
    for i in range(len(scheduleList)):        
        actionList.append(getAction(scheduleList[i]))
        print(actionList[i])
 
    return actionList
   

def buildPrecGraph(schedList):
    writeFlag = False
    n=len(schedList)

    #initialize graph
    matrixSize =findMaxTransNum(schedList)    
    precGraph = GRAPH(matrixSize+1) # will simply ignore the 0 row/column

    #add edges as needed per precedence
    for i in range(n):
        currTransNum = schedList[i].transactionNum
        currItem = schedList[i].item
        currType = schedList[i].actionType
           
        for j in range(i+1,n):
            if (schedList[j].transactionNum != currTransNum) and (schedList[j].item == currItem) and (currType == 'W' or schedList[j].actionType == 'W'):
                    precGraph.addEdge(currTransNum,schedList[j].transactionNum)

    return precGraph               


def findMaxTransNum(schedList):
    max=0

    for i in range(len(schedList)):
        max = schedList[i].transactionNum if schedList[i].transactionNum > max else max

    return max


def main():  
    scheduleStr = input("Enter an action schedule: ")
    scheduleList = parseSchedule(scheduleStr)   
    precGraph = buildPrecGraph(scheduleList)
    precGraph.printGraph()

    #check graph for cycle
    # if no cycle, return topological sort


if __name__ == "__main__":
    main()