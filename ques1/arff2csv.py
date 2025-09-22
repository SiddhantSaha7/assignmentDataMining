import csv

f = open("1_weather-numeric.arff", 'r')
lines = f.readlines()
headers = []
content = []
fileName = ''

for l in lines:
    if l.startswith("@relation"):
        fileName = f" {l.split(' ')[1].strip()}.csv"

    elif l.startswith("@attribute"):
        headers.append(l.split()[1].strip())
    
    elif l.startswith("@") or l.startswith("%") or l.startswith('\n'):
        continue
    
    else:
        content.append(l.strip().split(','))
        
with open(fileName, 'w') as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(headers)
    csvWriter.writerows(content)

f.close()