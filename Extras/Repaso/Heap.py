from BST import LinkedList
import math
class Heap:
    def __init__(self):
        pass
    def build(self,LL):
        n = LL.getLength()
        h = math.ceil( math.log2( n + 1) )
        mi = int(math.pow(2, h-1) - 1)
        mf = mi * 2 
        w = mf + 1
    
        matriz = [["&nbsp" for i in range(0,w)] for j in range(0,h)]
        half = math.floor(w/2)
        count = 0
        matriz[0][half] = LL.atPosition(count)
        count += 1
        for i in range(1,h):
            bs = int (math.pow(2,h-i) - 1)
            bsi = math.floor( bs/2 )
            j=0
            while(j<w):
                if(j==0):
                    j += bsi
                    matriz[i][j] = LL.atPosition(count)
                    count += 1
                elif(j+bs < w and count<=n):
                    j += bs
                    matriz[i][j] = LL.atPosition(count)
                    count += 1
                j+=1
        self.MakeHTMLHeap(matriz)

    def MakeHTMLHeap(self, matrix):
        f = open("Extras//Repaso//indexHeap.html","w")
        htmlStr = self.htmlTable(matrix)
        f.write(htmlStr)
        f.close()

    def htmlTable(self,matrix):
        htmlArr = ["<table border='5'>"]
        for r in matrix:
            row = []
            for value in r:
                row.append(str(value))
            htmlArr.append("<tr><td>")
            htmlArr.append("</td><td>".join(row))
            htmlArr.append("</td></tr>")
        htmlArr.append("</table>")
        return "".join(htmlArr)


'''
h = Heap()
l = LinkedList()
l.add(5)
l.add(2)
l.add(7)
l.add(1)
l.add(4)
l.add(6)
l.add(8)
h.build(l)
'''