import csv
import sys

# Reading csv file system arguement
csvFile = sys.argv[1]

# lists for storing the attributes, content of files and string for storing. filename
attributes = []
content = []
fileName = csvFile.split('.')[0]

#print first line of arff file
print("@relation "+fileName)

# reading csv to store attributes and content
with open(csvFile, mode ='r')as file:
    csvReader = csv.DictReader(file)
    attributes = csvReader.fieldnames
    for line in csvReader:
        content.append(list(line.values()))

# transpose of content to get all column values in a list
transpose_content = list(zip(*content))

# iterating over all attributes to print attribute lines of an arff file
for i in range(len(attributes)):
    output_string = "@attribute "+attributes[i] + " {"
    attribute_vals = set()
    numeric = False
    # getting unique values of each attribute to add to the line
    for j in transpose_content[i]:
        attribute_vals.add(j)
    for j in attribute_vals:
        #checking if its a numeric column
        if j.isdigit():
            numeric = True
            break
        else:
            output_string += j + ', '

    #finalizing the attribute line for arff file and printing it        
    if numeric == False:
        output_string= output_string[:-2]
        output_string+="}"
    else:
        output_string = output_string[:-1]
        output_string += "numeric"
    print(output_string)

print("@data")

#printing the data
for i in content:
    print(",".join(i)) 