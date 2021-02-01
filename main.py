
import re
from action import ACTION

def getAction(actionStr):    
    actionStr = actionStr.strip() 
    obj  = re.match(r'(?P<AcType>[R|W])(?P<TrNum>\d+)\((?P<AcItem>.*)\)', actionStr)

    return ACTION(obj.group(1),obj.group(2),obj.group(3))


def parseSequence(seqStr):
    actionList=[]

    seqStr = seqStr.strip()
    sequenceList = seqStr.split(';')
    
    for i in range(len(sequenceList)):        
        actionList.append(getAction(sequenceList[i]))
        print(actionList[i])
 
    return actionList


def main():  
    sequence_str = input("Enter an action sequence: ")
    actionList = parseSequence(sequence_str)
   
    # build graph of 
    #check graph for cycle
    # if no cycle, return topological sort


if __name__ == "__main__":
    main()