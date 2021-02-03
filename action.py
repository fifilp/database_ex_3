class ACTION:    
    actionType = None       #'R' or 'W'
    transactionNum = None   # 1,2...,n
    item = None             # the item the action is applied to


    def __init__(self, type,transNum, item):
        self.transactionNum = transNum
        self.actionType = type
        self.item = item


    def __str__(self):
        result = ""
        result += self.actionType+str(self.transactionNum)+self.item

        return result      
