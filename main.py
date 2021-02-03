
# databases Ex 03:
# this program checks if an input of a schedule of transaction operations
# is conflict serializable, and if yes, returns the serial order of the transactions
# We assume the input is a valid schedule.

import re
import queue
from action import ACTION
from graph import GRAPH


def findMaxTransNum(schedList):
    """this function returns the upper range of the transaction numbers"""
    max = 0

    for action in schedList:
        max = action.transactionNum if action.transactionNum > max else max

    return max

 
def getAction(actionStr):
    """this function receives a single action as string and returns it as an ACTION object"""
    actionStr = actionStr.strip()

    actionObject = re.match(
        r'(?P<AcType>[R|W])(?P<TrNum>\d+)\((?P<AcItem>.*)\)', actionStr)
    actionType = actionObject.group("AcType")
    transactionNum = int(actionObject.group("TrNum"))
    actionItem = actionObject.group("AcItem")

    return ACTION(actionType, transactionNum, actionItem)


def parseSchedule(schedStr):
    """this function parses the input string and returns a list of actions as objects"""
    actionList = []

    schedStr = schedStr.strip()
    scheduleList = schedStr.split(';')

    for actionStr in scheduleList:
        actionList.append(getAction(actionStr))

    return actionList


def buildPrecGraph(schedList):
    """this function builds a precedence graph based on the conflicts found in the schedule"""
    n = len(schedList)

    # initialize graph
    matrixSize = findMaxTransNum(schedList)
    precGraph = GRAPH(matrixSize)

    # add edges per precedence
    for i in range(n):
        currTransNum = schedList[i].transactionNum
        currItem = schedList[i].item
        currType = schedList[i].actionType

        for j in range(i + 1, n):
            if (schedList[j].transactionNum != currTransNum) \
                and (schedList[j].item == currItem) \
                    and (currType == 'W' or schedList[j].actionType == 'W'):
                precGraph.addEdge(currTransNum - 1,
                                  schedList[j].transactionNum - 1)

    return precGraph


def TopologicalSort(graph):
    """this function receives a graph and returns a toological sort if available"""
    topoSortList = []
    indegree = graph.getIndegreeList()

    # initializing queue of sources
    sourceQ = queue.Queue(graph.size)
    for i in range(len(indegree)):
        if indegree[i] == 0:
            sourceQ.put(i)

    while not sourceQ.empty():
        u = sourceQ.get()
        # +1 to convert from matrix index to transactionNum
        topoSortList.append(f'T{u + 1}')
        uAdjList = graph.getVertexAdjList(u)
        for v in uAdjList:
            indegree[v] -= 1
            if indegree[v] == 0:
                sourceQ.put(v)

    # if there's a vertex with degree!=0 at this point, there's a cycle
    # so there's no topological sort and we'll return an empty list
    for degree in indegree:
        if degree != 0:
            return []

    return topoSortList


def main():
    # read schedule from user
    scheduleStr = input("Enter an action schedule: ")
    # parse schedule and return a list of action objects
    scheduleList = parseSchedule(scheduleStr)
    # build precedence graph by checking the schedule for conflicts
    precGraph = buildPrecGraph(scheduleList)    
    # topologically sort precedence graph
    sortedList = TopologicalSort(precGraph)
    # the function will return a list of the sorted transactions
    # or an empty list if there's a cycle in the graph
    if sortedList:
        print(*sortedList, sep="->")
    else:        
        print("NO")


if __name__ == "__main__":
    main()
