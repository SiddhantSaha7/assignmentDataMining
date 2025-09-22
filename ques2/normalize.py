import sys

try:
    fileName = sys.argv[1]
    f = open(fileName)
    lb = int(sys.argv[2])
    ub = int(sys.argv[3])
    acc = int(sys.argv[4])

except:
    print("Input given is wrong")
    sys.exit(1)

lines = f.readlines()

data = []

for l in lines:
    nums = l.strip().split()
    nums = [float(x) for x in nums]
    data.append(nums)

transposed_data = list(zip(*data))
min_vals = [min(x) for x in transposed_data]
max_vals = [max(x) for x in transposed_data]

data_normalized = []

for row in data:
    arr_normalized = []
    for ind in range(0, len(row)):
        norm_val = lb + ( ( ( row[ind] - min_vals[ind] ) * (ub - lb) ) / (max_vals[ind] - min_vals[ind]) )
        arr_normalized.append(f"{norm_val:.{acc}f}")
    data_normalized.append(arr_normalized)

print(data_normalized)