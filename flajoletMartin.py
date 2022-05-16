inputList = [1, 3, 2, 1, 2, 3, 4, 3, 1, 2, 3, 1]
binaryList = []
rList = []


def h_function(x):
    return ((6 * x) + 1) % 5


def decimalToBinary(x):
    return bin(x)


for i in inputList:
    binaryList.append(decimalToBinary(h_function(i)))

for i in binaryList:
    if(i != "0b0"):
        nZeros = int(i.count("0")) - 1
    else:
        nZeros = 0
    rList.append(nZeros)
#Driver
dElements = max(rList) ** 2
print("The estimated number of distinct elements is: " + str(dElements))