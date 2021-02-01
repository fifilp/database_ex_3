class ACTION:    
    actionType = None   #'R' or 'W' enum or define? delete later
    transactionNum = None
    item = None         # item action is applied to

    def __init__(self, type,transNum, item):
        self.transactionNum = transNum
        self.actionType = type
        self.item = item

    def __str__(self):
        result = ""
        result += self.actionType+self.transactionNum+self.item

        return result      
