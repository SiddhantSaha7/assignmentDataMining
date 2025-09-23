import sys

#opening the file, storing the cli arguements and checking if they are ok
try:
    fileName = sys.argv[1]
    f = open(fileName)
    lb = int(sys.argv[2])
    ub = int(sys.argv[3])
    acc = int(sys.argv[4])

except:
    print("Input given is wrong")
    sys.exit(1)

# reading the lines of the file
lines = f.readlines()

data = []

#iterating over the file
for l in lines:
    nums = l.strip().split()
    nums = [float(x) for x in nums]
    #storing the file data in a matrix
    data.append(nums)

# transposing the matrix to be able to perform column vise normalization
transposed_data = list(zip(*data))
min_vals = [min(x) for x in transposed_data]
max_vals = [max(x) for x in transposed_data]

data_normalized = []

#iterating over the data
for row in data:
    arr_normalized = []
    for ind in range(0, len(row)):
        # normalized value calculation using the min and max that we calculated for each column/attribute
        norm_val = lb + ( ( ( row[ind] - min_vals[ind] ) * (ub - lb) ) / (max_vals[ind] - min_vals[ind]) )
        arr_normalized.append(f"{norm_val:.{acc}f}")
    data_normalized.append(arr_normalized)

#printing the normalized data
print(data_normalized)