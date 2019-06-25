fileStr = "1pac\\1.4-File & Stream\\data.csv"
myFile = open(fileStr,"r")
myFileStr = myFile.read()
rows = myFileStr.split("\n")
matrix = []
for row in rows:
    columns = row.split(",")
    matrix.append(columns)

print(matrix)