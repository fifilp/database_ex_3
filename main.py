
import re
import queue
from action import ACTION
from graph import GRAPH


def getAction(actionStr):
    actionStr = actionStr.strip()
    obj = re.match(
        r'(?P<AcType>[R|W])(?P<TrNum>\d+)\((?P<AcItem>.*)\)', actionStr)
    acType = obj.group("AcType")
    trNum = int(obj.group("TrNum"))
    acItem = obj.group("AcItem")

    return ACTION(acType, trNum, acItem)


def parseSchedule(schedStr):
    actionList = []

    schedStr = schedStr.strip()
    scheduleList = schedStr.split(';')

    for actionStr in scheduleList:
        actionList.append(getAction(actionStr))

    return actionList


def buildPrecGraph(schedList):
    n = len(schedList)

    # initialize graph
    matrixSize = findMaxTransNum(schedList)
    precGraph = GRAPH(matrixSize)  # we'll simply ignore the 0 row/column

    # add edges as needed per precedence
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


def findMaxTransNum(schedList):
    max = 0

    for action in schedList:
        max = action.transactionNum if action.transactionNum > max else max

    return max


def TopologicalSort(graph):
    topoSortList = []

    indegree = graph.getIndegreeList()

    # creating queue of sources
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

    for degree in indegree:
        if degree != 0:
            return []

    return topoSortList


def main():
    # read schedule from user
    scheduleStr = input("Enter an action schedule: ")
    # parse schedule and return a list of action objects
    scheduleList = parseSchedule(scheduleStr)
    # build precedence graph by scanning the schedule for conflicts
    precGraph = buildPrecGraph(scheduleList)
    precGraph.printGraph() # delete later - only for debugging
    # topologicaly sort precedence graph.
    sortedList = TopologicalSort(precGraph)
    # the function will return a list of the sorted transactions
    # or an empty list if there's a cycle in the graph
    if sortedList:
        print(*sortedList, sep="->")
    else:        
        print("NO")


if __name__ == "__main__":
    main()
