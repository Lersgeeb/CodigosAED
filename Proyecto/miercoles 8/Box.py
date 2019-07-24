from Node import *
from Clip import *
from CopyEraser import *
from Eraser import *
from Folder import *
from Marker import *
from Pen import *
from PostIt import *
from ReamOfPaper import *
from Staple import *
from Tape import *
from Stapler import *

class Box:
    
    def __init__(self):
        self.first = None
    
    def add(self,value):
        if(not self.first):
            self.first = Node(value)
            return True
        else:
            current=self.first
            while(current.next):
                current=current.next
            current.next= Node(value)
            return True
        
    def showContent(self):

        pens = 0
        erasers = 0
        clips = 0
        copyErasers = 0
        folders = 0
        markers = 0
        postIts = 0
        reamsofpaper = 0
        staples = 0
        staplers = 0
        tapes = 0
        current=self.first

        while(current.next):
            if(isinstance(current.value,Pen)):
                pens += 1 
            
            if(isinstance(current.value,Eraser)):
                erasers += 1 
            
            if(isinstance(current.value,Clip)):
                clips += 1 

            if(isinstance(current.value,CopyEraser)):
                copyErasers += 1 

            if(isinstance(current.value, Folder)):
                folders += 1 
            
            if(isinstance(current.value,Marker)):
                markers += 1 
           
            if(isinstance(current.value,PostIt)):
                postIts += 1 
           
            if(isinstance(current.value,ReamOfPaper)):
                reamsofpaper += 1 
            
            if(isinstance(current.value,Staple)):
                staples += 1     
            
            if(isinstance(current.value,Stapler)):
                staplers += 1     
            
            if(isinstance(current.value,Tape)):
                tapes += 1   

            current = current.next

        if(isinstance(current.value,Pen)):
            pens += 1 
        
        if(isinstance(current.value,Eraser)):
            erasers += 1 
        
        if(isinstance(current.value,Clip)):
            clips += 1 

        if(isinstance(current.value,CopyEraser)):
            copyErasers += 1 

        if(isinstance(current.value, Folder)):
            folders += 1 
        
        if(isinstance(current.value,Marker)):
            markers += 1 
        
        if(isinstance(current.value,PostIt)):
            postIts += 1 
        
        if(isinstance(current.value,ReamOfPaper)):
            reamsofpaper += 1 
        
        if(isinstance(current.value,Staple)):
            staples += 1     
        
        if(isinstance(current.value,Stapler)):
            staplers += 1     
        
        if(isinstance(current.value,Tape)):
            tapes += 1 

        print("\n----Contenido caja-----\nLapices: %s\nBorrador: %s\nClips: %s\ncopyEraser: %s\nMarcadores: %s\nFolders: %s\nPost-its: %s\nResmas de papel: %s\nGrapas: %s\nGrapadoras: %s\nTapes: %s\n---------------------------\n" % (pens,erasers,clips,copyErasers,markers,folders,postIts,reamsofpaper,staples,staplers,tapes))

    def addInPosition(self,value,n):
        if(n==0):
            queue=self.first
            self.first=Node(value)
            self.first.next=queue
            return True
        else:
            count=0
            queue=self.first
            while(queue.next):
                beforeQ=queue
                queue=queue.next
                count += 1
                if(count == n):
                    beforeQ.next=Node(value)
                    beforeQ.next.next=queue
                    return True
            count+=1
            if(count == n):
                queue.next=Node(value)
                return True
            print("No se encontro Posicion")
            return False

    def itsEmpty(self):
       return self.first == None 