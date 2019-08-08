filename = "Extras\\PythonTurtle\\Instru.txt"
file = open(filename,"r")
    
for line in file:
    
    lastline = line.strip

print(lastline)
    
file.seek(0)
command = file.readline()
print(command)
print(command)
print(command.strip()) 
print(command.strip())



    