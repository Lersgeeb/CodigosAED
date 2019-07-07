import random
import math

def random2Int(max = 100, min = 0):
    myInt = int(random.random()*(max-min)+min)
    myInt= math.floor(myInt)

    return myInt
 
class RandomCSV:
    
    def generateCSV(self):
        c = random2Int(15,10)
        r = random2Int(15,10)
        rows = []
        for i in range(0,c,1):
            columns = []
            for j in range(0,r,1):
                columns.append(str(random2Int(10,100)))
            
            rows.append(",".join(columns))

        return "\n".join(rows)




    