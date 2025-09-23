import sys
import time

# for tracking the execution time
startTime = time.perf_counter()

# reading cli arguements and ensuring they are correct
try:
    fileName = sys.argv[1]
    datFile = open(fileName)

except:
    print("File not found!")

#creating the arff file
arffFileName = fileName.split('.')[0]
arffFile = open(arffFileName+".arff", 'w')
arffFile.write(f"@RELATION {arffFileName}\n")

# for storing arff data
arffData = []
total_cols = 0

# iterating over dat file
for lines in datFile.readlines():
    #getting unique values in a line of the dat file
    data = set(lines.strip().split())
    #converting to list to be able to sort the data
    data = list([int(x) for x in data])
    data.sort()
    # creating line of format "{col1 1, col2 1, col3 1.....}"
    arffLine = "{"
    for col in data:
        arffLine += f"{col - 1} 1, "
        if col > total_cols:
            total_cols = col

    arffLine = arffLine.strip()[:-1] + "}\n"
    arffData.append(arffLine)

#Creating the beginning attributes of the arff file
for attribute in range(1, total_cols+1):
    arffFile.write(f"@ATTRIBUTE i{attribute} {{0, 1}}\n")

arffFile.write("@DATA\n")

#Writing the data in the arff file
for line in arffData:
    arffFile.write(line)

arffFile.close()

#calculating the runtime
endTime = time.perf_counter()
print(f"Total time taken to run the script: {endTime - startTime} seconds")
