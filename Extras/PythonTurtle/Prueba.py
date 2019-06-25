filename = "Extras\\PythonTurtle\\Instru.txt"
file = open(filename,"r")
    
for line in file:
    
    print(line)
    text = line.strip()
    commandList = text.split(",")
    # get the drawing command
    command = commandList[0]
    print("hola")
    print(command)


    