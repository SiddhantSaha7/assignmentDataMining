import sys
import time

startTime = time.perf_counter()

try:
    fileName = sys.argv[1]
    datFile = open(fileName)

except:
    print("File not found!")

arffFileName = fileName.split('.')[0]
arffFile = open(arffFileName+".arff", 'w')
arffFile.write(f"@RELATION {arffFileName}\n")

arffData = []
total_cols = 0

for lines in datFile.readlines():
    data = set(lines.strip().split())
    data = list([int(x) for x in data])
    data.sort()
    arffLine = "{"
    for col in data:
        arffLine += f"{col - 1} 1, "
        if col > total_cols:
            total_cols = col

    arffLine = arffLine.strip()[:-1] + "}\n"
    arffData.append(arffLine)

for attribute in range(1, total_cols+1):
    arffFile.write(f"@ATTRIBUTE i{attribute} {{0, 1}}\n")

arffFile.write("@DATA\n")

for line in arffData:
    arffFile.write(line)

arffFile.close()

endTime = time.perf_counter()
print(f"Total time taken to run the script: {endTime - startTime} seconds")
