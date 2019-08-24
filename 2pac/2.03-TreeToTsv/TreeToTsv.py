def treeToTsv(current,tab=0):
    trail = ""
    while(current):
        if(current.value[-1]=="/"):
            trail = "%s%s%s\n" % (trail,"\t"*tab,current.value)
            trail = "%s%s" % (trail,treeToTsv(current.children.first,tab+1))
        else:
            trail = "%s%s%s\n" % (trail,"\t"*tab,current.value)
        current = current.next
    return trail
    
def treeTofile(tree,filename):
    tsvStr = treeToTsv(tree.root)
    f = open(filename,"w")
    f.write(tsvStr)
    f.close()
    return True